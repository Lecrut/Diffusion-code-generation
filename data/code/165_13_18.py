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

def validate_contacts(contacts):
    if not all(isinstance(contact, Contact) for contact in contacts):
        raise ValueError("All elements in the contacts list must be instances of Contact")

def serialize_contacts(contacts):
    validate_contacts(contacts)
    return json.dumps([contact.to_dict() for contact in contacts], indent=4)

if __name__ == '__main__':
    sample_contacts = [
        Contact('Alice', '123-456-7890'),
        Contact('Bob', '987-654-3210')
    ]
    print(serialize_contacts(sample_contacts))