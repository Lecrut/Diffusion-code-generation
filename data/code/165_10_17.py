class ContactBook:

    def __init__(self):
        self.contacts = {}

    def add(self, name, number):
        if name not in self.contacts:
            self.contacts[name] = number
            return True
        return False

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
    cb = ContactBook()
    print(cb.add('Alice', '123-456-7890'))
    print(cb.retrieve('Alice'))
    print(cb.update('Alice', '098-765-4321'))
    print(cb.retrieve('Alice'))
    print(cb.delete('Alice'))
    print(cb.retrieve('Alice'))