class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
class ContactBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self, contact):
        self.contacts.append(contact)
    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
if __name__ == '__main__':
    book = ContactBook()
    contact1 = Contact("Alice", "123-456-7890", "alice@example.com")
    contact2 = Contact("Bob", "987-654-3210", "bob@example.com")
    contact3 = Contact("Charlie", "555-123-4567", "charlie@example.com")
    book.add_contact(contact1)
    book.add_contact(contact2)
    book.add_contact(contact3)
    print("--- Contact Book ---")
    book.display_contacts()