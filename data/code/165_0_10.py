class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        if contact.name in self.contacts:
            raise ValueError("Contact already exists")
        self.contacts[contact.name] = contact

    def remove_contact(self, name):
        if name not in self.contacts:
            raise KeyError("Contact does not exist")
        del self.contacts[name]

    def get_contact(self, name):
        return self.contacts.get(name, None)

if __name__ == '__main__':
    book = ContactBook()
    alice = Contact("Alice", "123-456-7890", "alice@example.com")
    book.add_contact(alice)
    print(book.get_contact("Alice"))
    book.remove_contact("Alice")
    print(book.get_contact("Alice") is None)