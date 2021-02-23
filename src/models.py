import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()



class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    UserID = Column(Integer, primary_key=True)
    password = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    


class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    gender = Column(String(200))
    skin_color = Column(String(200))
    eye_color = Column(String(200))
    hair_color = Column(String(200))
    height = Column(String(200))
    homeworld = Column(String(200))
       
    
class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    gravity = Column(String(250))
    orbital_period = Column(Integer)
    population = Column(Integer)
    rotation_period= Column(Integer)
    terrain = Column(String(250))

class Favorites(Base):
    __tablename__ = 'Favorite'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID_Favorite = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('user.UserID'))
    user = relationship(User)
    name = Column(String(50), nullable=False)
    people_ID = Column(Integer, ForeignKey('people.id'))
    peoples = relationship(People)
    planet_ID = Column(Integer, ForeignKey('planets.id'))
    Planet = relationship(Planets)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram2.png')