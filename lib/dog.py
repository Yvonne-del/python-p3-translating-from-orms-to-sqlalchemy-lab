from models import Dog
from sqlalchemy import (Column, String, Integer, create_engine)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_table(base, engine):
    Base.metadata.create_all(engine)


def save(session, dog):
    session.add(dog)
    session.commit()


def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name ==name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    for d in session.query(Dog):
        d.dog = dog
        d.breed = breed