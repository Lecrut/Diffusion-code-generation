class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        if name in self.contacts:
            raise ValueError("Contact already exists")
        self.contacts[name] = number

    def get_contact(self, name):
        return self.contacts.get(name, "Contact not found")

    def update_contact(self, name, number):
        if name not in self.contacts:
            raise ValueError("Contact does not exist")
        self.contacts[name] = number

    def delete_contact(self, name):
        if name not in self.contacts:
            raise ValueError("Contact does not exist")
        del self.contacts[name]

if __name__ == '__main__':
    cb = ContactBook()
    cb.add_contact("Alice", "1234567890")
    print(cb.get_contact("Alice"))
    cb.update_contact("Alice", "0987654321")
    print(cb.get_contact("Alice"))
    cb.delete_contact("Alice")
    print(cb.get_contact("Alice"))