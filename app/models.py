from datetime import datetime

from . import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    reviews = db.relationship('Review', back_populates='movie')

    def __repr__(self):
        return f'Фильм {self.id}: ({self.title})'


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    score = db.Column(db.Integer, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id', ondelete="CASCADE"))
    movie = db.relationship('Movie', back_populates='reviews')

    def __repr__(self):
        return f'Отзыв {self.id}: ({self.title[:20]}...)'
