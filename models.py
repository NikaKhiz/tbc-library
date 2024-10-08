from sqlalchemy import Column, Integer, Date, ForeignKey, String, create_engine
from sqlalchemy.orm import declarative_base, relationship


db_url = 'sqlite:///library.db' 
engine = create_engine(db_url)
Base = declarative_base()


class Author(Base):
    __tablename__ = 'author' 

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    books = relationship('Book', secondary="author_book", back_populates='author', cascade='all, delete')


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey('author.id'))
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    release_date = Column(Date, nullable=False)
    author = relationship('Author', secondary="author_book", back_populates='books')


# junction table for authors and books
class AuthorBook(Base):
    __tablename__ = 'author_book'
    
    author_id = Column(Integer, ForeignKey('author.id'), primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)