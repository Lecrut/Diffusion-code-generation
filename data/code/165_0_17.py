class ContactBook:
    CONTACT_KEYS = {'phone', 'email'}

    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, details):
        if not self._is_valid_details(details):
            raise ValueError("Invalid contact details")
        if name in self.contacts:
            raise ValueError("Contact already exists")
        self.contacts[name] = details

    def remove_contact(self, name):
        if name not in self.contacts:
            raise KeyError("Contact does not exist")
        del self.contacts[name]

    def get_contact(self, name):
        return self.contacts.get(name, None)

    @staticmethod
    def _is_valid_details(details):
        return isinstance(details, dict) and all(key in ContactBook.CONTACT_KEYS for key in details)

if __name__ == '__main__':
    cb = ContactBook()
    cb.add_contact('Alice', {'phone': '1234567890', 'email': 'alice@example.com'})
    print(cb.get_contact('Alice'))
    cb.remove_contact('Alice')