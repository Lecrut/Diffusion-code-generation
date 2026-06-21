import json

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone
        }

def serialize_contacts(contacts):
    encoder = json.JSONEncoder(default=lambda o: o.to_dict())
    return encoder.encode(contacts)

if __name__ == '__main__':
    contacts = [Contact("Alice", "123-456-7890"), Contact("Bob", "987-654-3210")]
    print(serialize_contacts(contacts))