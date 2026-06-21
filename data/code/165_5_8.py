import threading

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.lock = threading.Lock()

    def add_contact(self, name, number):
        with self.lock:
            self.contacts[name] = number

    def get_contact(self, name):
        with self.lock:
            return self.contacts.get(name)

if __name__ == '__main__':
    cb = ContactBook()
    cb.add_contact('Alice', '1234567890')
    print(cb.get_contact('Alice'))