import json

class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email
        }

def serialize_contacts(contacts):
    return json.dumps([contact.to_dict() for contact in contacts], default=lambda o: o.__dict__)

if __name__ == '__main__':
    contacts = [
        Contact('Alice', 'alice@example.com'),
        Contact('Bob', 'bob@example.com')
    ]
    print(serialize_contacts(contacts))