class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, details):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(details, dict):
            raise ValueError("Details must be a dictionary")
        if 'phone' not in details or 'email' not in details:
            raise ValueError("Details must contain 'phone' and 'email'")
        self.contacts[name] = details

    def remove_contact(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        if name not in self.contacts:
            raise KeyError(f"Contact '{name}' does not exist")
        del self.contacts[name]

    def get_contact(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        return self.contacts.get(name, None)

if __name__ == '__main__':
    cb = ContactBook()
    try:
        cb.add_contact('Alice', {'phone': '1234567890', 'email': 'alice@example.com'})
        print(cb.get_contact('Alice'))
        cb.remove_contact('Alice')
    except Exception as e:
        print(e)