class ContactBook:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, name, phone, email):
        self.contacts[name] = {"phone": phone, "email": email}
    def display_contact(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"Name: {name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        else:
            print(f"Contact {name} not found.")
if __name__ == '__main__':
    book = ContactBook()
    book.add_contact("Alice", "123-456-7890", "alice@example.com")
    book.add_contact("Bob", "987-654-3210", "bob@example.com")
    book.add_contact("Charlie", "555-123-4567", "charlie@example.com")
    book.display_contact("Alice")
    book.display_contact("Bob")
    book.display_contact("David")