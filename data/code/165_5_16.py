import threading

class ContactBook:
    DEFAULT_CONTACT = "Unknown"

    def __init__(self):
        self.contacts = {}
        self.lock = threading.Lock()

    def add_contact(self, name, number):
        with self.lock:
            if name not in self.contacts:
                self.contacts[name] = number

    def get_contact(self, name):
        with self.lock:
            return self.contacts.get(name, ContactBook.DEFAULT_CONTACT)

if __name__ == '__main__':
    cb = ContactBook()
    cb.add_contact('Alice', '123-456-7890')
    print(cb.get_contact('Alice'))
    print(cb.get_contact('Bob'))