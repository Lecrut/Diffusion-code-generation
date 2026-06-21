import json

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone
        }

def serialize_contacts(contacts):
    if not all(isinstance(contact, Contact) for contact in contacts):
        raise ValueError("All elements in the list must be instances of Contact")
    return json.dumps([contact.to_dict() for contact in contacts], indent=4)

if __name__ == '__main__':
    contacts = [
        Contact('Alice', '123-456-7890'),
        Contact('Bob', '987-654-3210')
    ]
    print(serialize_contacts(contacts))