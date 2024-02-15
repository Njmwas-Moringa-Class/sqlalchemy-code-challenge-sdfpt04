import os
import sys
from sqlalchemy import create_engine, PrimaryKeyConstraint, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine('sqlite:///db/restaurants.db', echo=True)

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    def __repr__(self):
        return f'Review: {self.star_rating} stars'

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)
    
    reviews = relationship("Review", back_populates="restaurant")

    def __repr__(self):
        return f'Restaurant: {self.name}'

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    reviews = relationship("Review", back_populates="customer")

    def __repr__(self):
        return f'Customer: {self.first_name} {self.last_name}'

# Create tables
Base.metadata.create_all(engine)
