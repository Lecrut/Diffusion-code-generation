class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if not all([name, phone, email]):
            raise ValueError("Name, phone, and email are required")
        if name in self.contacts:
            raise ValueError(f"Contact '{name}' already exists")
        self.contacts[name] = {'phone': phone, 'email': email}

    def remove_contact(self, name):
        if not name:
            raise ValueError("Name is required")
        if name not in self.contacts:
            raise KeyError(f"Contact '{name}' does not exist")
        del self.contacts[name]

    def get_contact(self, name):
        if not name:
            raise ValueError("Name is required")
        return self.contacts.get(name, None)

if __name__ == '__main__':
    cb = ContactBook()
    cb.add_contact('Alice', '123-456-7890', 'alice@example.com')
    print(cb.get_contact('Alice'))
    cb.remove_contact('Alice')