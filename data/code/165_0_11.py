class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, details):
        if not isinstance(details, dict) or 'phone' not in details or 'email' not in details:
            raise ValueError("Invalid contact details")
        if name in self.contacts:
            raise ValueError("Contact already exists")
        self.contacts[name] = Contact(name, details['phone'], details['email'])

    def remove_contact(self, name):
        if name not in self.contacts:
            raise KeyError("Contact does not exist")
        del self.contacts[name]

    def get_contact(self, name):
        return self.contacts.get(name, None)

if __name__ == '__main__':
    cb = ContactBook()
    try:
        cb.add_contact('Alice', {'phone': '1234567890', 'email': 'alice@example.com'})
        print(cb.get_contact('Alice'))
        cb.remove_contact('Alice')
    except Exception as e:
        print(e)