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
    contacts = [
        {'name': 'Alice', 'phone': '123-456-7890'},
        {'name': 'Bob', 'phone': '098-765-4321'},
        {'name': 'Charlie', 'phone': '111-222-3333'}
    ]
    iterator = ContactIterator(contacts)
    for contact in iterator:
        print(contact)