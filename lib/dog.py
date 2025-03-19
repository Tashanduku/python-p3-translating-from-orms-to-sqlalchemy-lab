from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from lib.models import Dog, Base

SQLITE_URL = "sqlite:///dogs.db"

def create_table(base, engine):
    """Creates a SQLite database using the given declarative_base."""
    base.metadata.create_all(engine)

def save(session, dog):
    """Saves a Dog instance to the database and ensures it's the only entry."""
    session.query(Dog).delete() 
    session.add(dog)
    session.commit()

def get_all(session):
    """Returns all Dog instances from the database."""
    return session.query(Dog).all()

def find_by_name(session, name):
    """Finds a dog by name."""
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, dog_id):
    """Finds a dog by ID."""
    return session.query(Dog).filter_by(id=dog_id).first()

def find_by_name_and_breed(session, name, breed):
    """Finds a dog by name and breed."""
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, new_breed):
    """Updates the breed of the given dog."""
    dog.breed = new_breed
    session.commit()
