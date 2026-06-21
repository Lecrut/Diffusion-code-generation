class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, details):
        self.contacts[name] = details

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def get_contact(self, name):
        return self.contacts.get(name, None)

if __name__ == '__main__':
    cb = ContactBook()
    cb.add_contact('Alice', {'email': 'alice@example.com', 'phone': '123-456-7890'})
    print(cb.get_contact('Alice'))
    cb.remove_contact('Alice')
    print(cb.get_contact('Alice'))