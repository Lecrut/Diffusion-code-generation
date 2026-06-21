class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __repr__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

def sort_books(books):
    return sorted(books, key=lambda book: book.year)

if __name__ == '__main__':
    books = [
        Book("1984", "George Orwell", 1949),
        Book("To Kill a Mockingbird", "Harper Lee", 1960),
        Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
        Book("Pride and Prejudice", "Jane Austen", 1813)
    ]
    sorted_books = sort_books(books)
    print(sorted_books)