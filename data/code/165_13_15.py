import json

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def to_dict(self):
        return {"name": self.name, "phone": self.phone}

def serialize_contacts(contacts):
    contact_dicts = [contact.to_dict() for contact in contacts]
    return json.dumps(contact_dicts, default=lambda o: o.__dict__, separators=(',', ':'))

if __name__ == '__main__':
    contacts = [
        Contact("Alice", "123-456-7890"),
        Contact("Bob", "098-765-4321")
    ]
    print(serialize_contacts(contacts))