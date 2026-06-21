import threading

class ContactSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ContactSingleton, cls).__new__(cls)
                    cls.contacts = {}
        return cls._instance

    def add_contact(self, name, phone):
        with self._lock:
            self.contacts[name] = phone

    def get_contact(self, name):
        with self._lock:
            return self.contacts.get(name)
if __name__ == '__main__':
    singleton1 = ContactSingleton()
    singleton2 = ContactSingleton()
    singleton1.add_contact('Alice', '123-456-7890')
    print(singleton2.get_contact('Alice'))