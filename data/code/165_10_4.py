class ContactBook:

    def __init__(self):
        self.contacts = {}

    def add(self, name, phone_number):
        self.contacts[name] = phone_number

    def retrieve(self, name):
        return self.contacts.get(name, None)

    def update(self, name, new_phone_number):
        if name in self.contacts:
            self.contacts[name] = new_phone_number
            return True
        return False

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False
if __name__ == '__main__':
    cb = ContactBook()
    cb.add('Alice', '123-456-7890')
    print(cb.retrieve('Alice'))
    cb.update('Alice', '098-765-4321')
    print(cb.retrieve('Alice'))
    cb.delete('Alice')
    print(cb.retrieve('Alice'))