class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, number):
        self.contacts[name] = number

    def retrieve(self, name):
        return self.contacts.get(name, None)

    def update(self, name, new_number):
        if name in self.contacts:
            self.contacts[name] = new_number
            return True
        return False

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False

if __name__ == '__main__':
    contact_book = ContactBook()
    contact_book.add("Alice", "123-456-7890")
    print(contact_book.retrieve("Alice"))
    contact_book.update("Alice", "098-765-4321")
    print(contact_book.retrieve("Alice"))
    contact_book.delete("Alice")
    print(contact_book.retrieve("Alice"))