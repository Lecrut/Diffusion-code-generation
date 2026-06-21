import threading

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.lock = threading.Lock()

    def add_contact(self, name, number):
        with self.lock:
            if name in self.contacts:
                return False
            self.contacts[name] = number
            return True

    def get_contact(self, name):
        with self.lock:
            return self.contacts.get(name, None)

if __name__ == '__main__':
    cb = ContactBook()
    if cb.add_contact('Bob', '987-654-3210'):
        print(f"Contact added: {cb.get_contact('Bob')}")