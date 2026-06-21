import json

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

def serialize_contacts(contacts):
    return json.dumps([{'name': contact.name, 'phone': contact.phone} for contact in contacts], default=lambda o: o.__dict__)

if __name__ == '__main__':
    contacts = [Contact('Alice', '123'), Contact('Bob', '456')]
    print(serialize_contacts(contacts))