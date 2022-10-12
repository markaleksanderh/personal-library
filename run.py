from dotenv import dotenv_values
import requests

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///pl.db', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String)

# class Book(Base):
#     __tablename__ = 'books'


# class UserLibrary(Base):
#     pass


user = User(username="Mark")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add(user)
session.commit()

def get_book_by_ISBN(isbn):
    open_lib_url = 'http://openlibrary.org/api/books?bibkeys=ISBN:{}&jscmd=data&format=json'.format(isbn)
    res = requests.get(url = open_lib_url).json()
    return res

def main():
    # test_isbn = 1501183931
    # book = get_book_by_ISBN(test_isbn)
    # print(book)
    pass

if __name__ == '__main__':
    main()

