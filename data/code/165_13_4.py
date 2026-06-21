import json

class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email

def serialize_contacts(contacts):
    return json.dumps([{'name': contact.name, 'email': contact.email} for contact in contacts], default=lambda o: o.__dict__, separators=(',', ':'))

if __name__ == '__main__':
    contacts = [Contact('Alice', 'alice@example.com'), Contact('Bob', 'bob@example.com')]
    print(serialize_contacts(contacts))