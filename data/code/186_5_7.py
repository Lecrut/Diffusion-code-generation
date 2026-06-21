class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"{self.title} by {self.author}"

def sort_books_by_author(books):
    return sorted(books, key=lambda book: book.author)

if __name__ == '__main__':
    books = [
        Book("1984", "George Orwell"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("The Great Gatsby", "F. Scott Fitzgerald")
    ]
    sorted_books = sort_books_by_author(books)
    print(sorted_books)