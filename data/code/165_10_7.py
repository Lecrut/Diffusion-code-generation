class ContactBook:

    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number

    def get_contact(self, name):
        return self.contacts.get(name, None)

    def update_contact(self, name, new_phone_number):
        if name in self.contacts:
            self.contacts[name] = new_phone_number
            return True
        return False

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False
if __name__ == '__main__':
    cb = ContactBook()
    cb.add_contact('Alice', '123-456-7890')
    print(cb.get_contact('Alice'))
    cb.update_contact('Alice', '098-765-4321')
    print(cb.get_contact('Alice'))
    cb.delete_contact('Alice')
    print(cb.get_contact('Alice'))