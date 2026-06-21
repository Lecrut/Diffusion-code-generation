class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, number):
        if name in self.contacts:
            raise ValueError("Contact already exists")
        self.contacts[name] = number

    def retrieve(self, name):
        return self.contacts.get(name, None)

    def update(self, name, new_number):
        if name not in self.contacts:
            raise ValueError("Contact not found")
        self.contacts[name] = new_number

    def delete(self, name):
        if name not in self.contacts:
            raise ValueError("Contact not found")
        del self.contacts[name]

if __name__ == '__main__':
    cb = ContactBook()
    cb.add("Alice", "1234567890")
    print(cb.retrieve("Alice"))
    cb.update("Alice", "0987654321")
    print(cb.retrieve("Alice"))
    cb.delete("Alice")
    print(cb.retrieve("Alice"))