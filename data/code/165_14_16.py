import threading

class ContactSingleton:
    _instance = None
    _lock = threading.Lock()
    contacts = {}

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ContactSingleton, cls).__new__(cls)
        return cls._instance

    def add_contact(self, name, phone):
        if not name or not phone:
            raise ValueError("Name and phone number must be provided")
        with self._lock:
            self.contacts[name] = phone

    def get_contact(self, name):
        with self._lock:
            return self.contacts.get(name)

if __name__ == '__main__':
    singleton1 = ContactSingleton()
    singleton1.add_contact("John Doe", "1234567890")
    print(singleton1.get_contact("John Doe"))