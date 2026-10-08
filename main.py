from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
class Book(BaseModel):
    title: str
    author: str
    year: int

books = [
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    },
    {
        "id": 2,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937
    }
]


@app.get("/")
def home():
    return {"message": "Book API is working"}


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: Book):
    new_id = max(item["id"] for item in books) + 1

    new_book = {
        "id": new_id,
        "title": book.title,
        "author": book.author,
        "year": book.year
    }

    books.append(new_book)

    return new_book


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for book in books:
        if book["id"] == book_id:
            book["title"] = updated_book.title
            book["author"] = updated_book.author
            book["year"] = updated_book.year
            return book

    raise HTTPException(status_code=404, detail="Book not found")



@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}

    raise HTTPException(status_code=404, detail="Book not found")