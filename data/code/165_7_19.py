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

class Contact:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.name}: {self.phone}'
if __name__ == '__main__':
    contacts = [Contact('Alice', '123-456-7890'), Contact('Bob', '098-765-4321')]
    iterator = ContactIterator(contacts)
    print(next(iterator))
    print(next(iterator))