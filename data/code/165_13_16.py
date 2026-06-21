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
    return json.dumps([contact.to_dict() for contact in contacts], indent=4)

if __name__ == '__main__':
    sample_contacts = [
        Contact('Alice', '123-456-7890'),
        Contact('Bob', '987-654-3210'),
        Contact('Charlie', '555-555-5555')
    ]
    serialized_data = serialize_contacts(sample_contacts)
    print(serialized_data)