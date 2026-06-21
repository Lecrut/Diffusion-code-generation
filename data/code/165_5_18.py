import threading

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.lock = threading.Lock()

    def add_contact(self, name, number):
        if not isinstance(name, str) or not isinstance(number, str):
            raise ValueError("Both name and number must be strings")
        with self.lock:
            if name in self.contacts:
                raise KeyError(f"Contact {name} already exists")
            self.contacts[name] = number

    def get_contact(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        with self.lock:
            return self.contacts.get(name, None)

if __name__ == '__main__':
    cb = ContactBook()
    try:
        cb.add_contact('Alice', '123-456-7890')
        print(f"Contact added: {cb.get_contact('Alice')}")
        cb.add_contact('Bob', '987-654-3210')
        print(f"Contact added: {cb.get_contact('Bob')}")
    except (ValueError, KeyError) as e:
        print(e)