import threading

class ContactSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ContactSingleton, cls).__new__(cls)
                cls.contacts = {}
        return cls._instance

    def add_contact(self, name, number):
        with self._lock:
            self.contacts[name] = number

    def get_contact(self, name):
        with self._lock:
            return self.contacts.get(name)

if __name__ == '__main__':
    contact_manager = ContactSingleton()
    contact_manager.add_contact('Alice', '1234567890')
    print(contact_manager.get_contact('Alice'))