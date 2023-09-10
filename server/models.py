from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validates_name(self, key, value):
        if value == "":
            raise ValueError("Must have a name")
        return value

    @validates('phone_number')
    def validate_author_phonenumber(self, key, value):
        if len(value) != 10:
            raise ValueError("phone number must be 10 digits")
        return value

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'


class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content')
    def validates_content(self, key, value):
        if len(value) < 250:
            raise ValueError("post must at least have 250 characters")
        return value

    @validates('summary')
    def validates_summary(self, key, value):
        if len(value) >= 250:
            raise ValueError("post must at most have 250 characters")
        return value

    @validates('category')
    def validates_category(self, key, value):
        if value not in ["Fiction", "Non-Fiction"]:
            raise ValueError("post must be fiction or non-fiction")
        return value
    # this check is not required anymore!
    # @validates('title')
    # def validates_title(self, key, value):
    #     if value == "":
    #         raise ValueError("post must have a title")
    #     return value

    @validates('title')
    def validates_click_bait(self, key, value):
        clickbait_keywords = ["Won't Believe", "Secret",
                              "Top", "Guess"]
        if value not in clickbait_keywords:
            raise ValueError("title in noy click_bait-y")
        return value

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
