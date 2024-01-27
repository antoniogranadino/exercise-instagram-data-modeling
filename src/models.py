import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__= 'user'

    id = Column(Integer, primary_key = True)
    username = Column(String(50), nullable = False, unique = True)
    password = Column(String(250), nullable = False)
    post = relationship("Post", backref = "user")
    comment = relationship("Comment", backref = "user")
    like = relationship("Like", backref = "user")



class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key = True)
    description = Column(String(200))
    user_id = Column(Integer, ForeignKey("user.id"))
    comment = relationship("Comment", backref = "post")
    like = relationship("Like", backref = "post")


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key = True)
    replies = Column(String(500), nullable = False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable = False)
    like = relationship("Like", backref = "comment")



class Like(Base):
    __tablename__ = "like"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable = False)
    comment_id = Column(Integer, ForeignKey("comment.id"), nullable = False)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
