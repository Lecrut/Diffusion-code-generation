import threading

class ContactBook:
    DEFAULT_LOCK = threading.Lock()

    def __init__(self):
        self.contacts = {}
        self.lock = ContactBook.DEFAULT_LOCK

    def add_contact(self, name, number):
        with self.lock:
            if name not in self.contacts:
                self.contacts[name] = number

    def get_contact(self, name):
        with self.lock:
            return self.contacts.get(name, None)

if __name__ == '__main__':
    cb = ContactBook()
    cb.add_contact('Alice', '123-456-7890')
    print(cb.get_contact('Alice'))