import threading

class ContactSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ContactSingleton, cls).__new__(cls)
                    cls._contacts = {}
        return cls._instance

    def add_contact(self, name, phone):
        cls.validate_input(name, phone)
        with self._lock:
            self._contacts[name] = phone

    def get_contact(self, name):
        with self._lock:
            return self._contacts.get(name)

    @staticmethod
    def validate_input(name, phone):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        if not isinstance(phone, (int, str)) or not phone.strip():
            raise ValueError("Phone number must be a non-empty string")

if __name__ == '__main__':
    singleton = ContactSingleton()
    try:
        singleton.add_contact("Alice", "123-456-7890")
        print(singleton.get_contact("Alice"))
    except ValueError as e:
        print(e)