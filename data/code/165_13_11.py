import json

class Contact:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone
        }

def serialize_contacts(contacts):
    return json.dumps([contact.to_dict() for contact in contacts], indent=4)

if __name__ == '__main__':
    sample_contacts = [
        Contact(1, "Alice", "111-222-3333"),
        Contact(2, "Bob", "444-555-6666"),
        Contact(3, "Charlie", "777-888-9999")
    ]
    serialized_contacts = serialize_contacts(sample_contacts)
    print(serialized_contacts)