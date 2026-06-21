class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactIterator:
    def __init__(self, contacts):
        self.contacts = contacts
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.contacts):
            raise StopIteration
        contact = self.contacts[self.index]
        self.index += 1
        return contact

if __name__ == '__main__':
    contacts = [Contact("Alice", "1234567890"), Contact("Bob", "0987654321")]
    iterator = ContactIterator(contacts)
    
    for contact in iterator:
        print(f"Name: {contact.name}, Phone: {contact.phone}")