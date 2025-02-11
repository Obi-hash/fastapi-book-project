from typing import OrderedDict, Dict

from fastapi import APIRouter, HTTPException, status

from api.db.schemas import Book, Genre

router = APIRouter()


class InMemoryDB:
    def __init__(self):
        self.books: Dict[int, Book] = {
            1: Book(
                id=1,
                title="The Hobbit",
                author="J.R.R. Tolkien",
                publication_year=1937,
                genre=Genre.SCI_FI,
            ),
            2: Book(
                id=2,
                title="The Lord of the Rings",
                author="J.R.R. Tolkien",
                publication_year=1954,
                genre=Genre.FANTASY,
            ),
            3: Book(
                id=3,
                title="The Return of the King",
                author="J.R.R. Tolkien",
                publication_year=1955,
                genre=Genre.FANTASY,
            ),
        }

    def add_book(self, book: Book):
        self.books[book.id] = book

    def get_books(self) -> Dict[int, Book]:
        return self.books

    def update_book(self, book_id: int, book: Book) -> Book:
        if book_id not in self.books:
            raise HTTPException(status_code=404, detail="Book not found")
        self.books[book_id] = book
        return book

    def delete_book(self, book_id: int):
        if book_id not in self.books:
            raise HTTPException(status_code=404, detail="Book not found")
        del self.books[book_id]

    def get_book_by_id(self, book_id: int) -> Book:
        """Retrieve a book by its ID."""
        if book_id not in self.books:
            raise HTTPException(status_code=404, detail="Book not found")
        return self.books[book_id]


db = InMemoryDB()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    db.add_book(book)
    return book  # Returning book directly as a properly formatted JSON


@router.get("/", status_code=status.HTTP_200_OK)
async def get_books() -> Dict[int, Book]:
    return db.get_books()  # Returning dictionary of books as JSON


@router.get("/{book_id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: int):
    book = db.get_book_by_id(book_id)
    return book  # Returning book object directly


@router.put("/{book_id}", status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book: Book):
    updated_book = db.update_book(book_id, book)
    return updated_book  # Returning updated book object


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    db.delete_book(book_id)
    return None  # FastAPI automatically returns an empty response body























































































































































    










































    


    























































































































































































































































