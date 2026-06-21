import threading

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.lock = threading.Lock()

    def add_contact(self, name, number):
        with self.lock:
            if name not in self.contacts:
                self.contacts[name] = number

    def get_contact(self, name):
        with self.lock:
            return self.contacts.get(name, None)

if __name__ == '__main__':
    cb = ContactBook()
    contact_name = 'Bob'
    contact_number = '987-654-3210'
    cb.add_contact(contact_name, contact_number)
    print(cb.get_contact(contact_name))