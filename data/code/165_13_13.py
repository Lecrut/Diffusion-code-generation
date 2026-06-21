import json

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    @staticmethod
    def to_dict(contact):
        return {
            'name': contact.name,
            'phone': contact.phone
        }

def serialize_contacts(contacts):
    return json.dumps([Contact.to_dict(contact) for contact in contacts], indent=4)

if __name__ == '__main__':
    contacts = [
        Contact('Alice', '123-456-7890'),
        Contact('Bob', '987-654-3210')
    ]
    print(serialize_contacts(contacts))