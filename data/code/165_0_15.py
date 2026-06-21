class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            raise ValueError("Contact already exists")
        self.contacts[name] = {'phone': phone, 'email': email}

    def remove_contact(self, name):
        if name not in self.contacts:
            raise KeyError("Contact does not exist")
        del self.contacts[name]

    def get_contact(self, name):
        return self.contacts.get(name, None)

if __name__ == '__main__':
    cb = ContactBook()
    cb.add_contact('Alice', '123-456-7890', 'alice@example.com')
    print(cb.get_contact('Alice'))
    cb.remove_contact('Alice')