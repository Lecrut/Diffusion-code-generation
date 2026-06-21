import threading

class ContactSingleton:
    _instance = None
    _lock = threading.Lock()
    CONTACTS_KEY = 'contacts'

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ContactSingleton, cls).__new__(cls)
                setattr(cls._instance, cls.CONTACTS_KEY, {})
        return cls._instance

    @staticmethod
    def _get_contacts(instance):
        return getattr(instance, ContactSingleton.CONTACTS_KEY)

    def add_contact(self, name, phone):
        with self._lock:
            contacts = self._get_contacts(self)
            contacts[name] = phone

    def get_contact(self, name):
        with self._lock:
            contacts = self._get_contacts(self)
            return contacts.get(name)

if __name__ == '__main__':
    singleton1 = ContactSingleton()
    singleton1.add_contact('Alice', '123-456-7890')
    print(singleton1.get_contact('Alice'))