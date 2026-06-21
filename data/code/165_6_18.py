import json

class ContactSerializer:
    def __init__(self):
        self.filename = 'contacts.json'

    def serialize_contacts(self, contacts):
        with open(self.filename, 'w') as file:
            json.dump([{'name': contact.get('name', ''), 'phone': contact.get('phone', ''), 'email': contact.get('email', '')} for contact in contacts], file)

    def deserialize_contacts(self):
        with open(self.filename, 'r') as file:
            return [contact for contact in json.load(file)]

if __name__ == '__main__':
    serializer = ContactSerializer()
    contacts = [{'name': 'Alice', 'phone': '1234567890'}, {'email': 'bob@example.com'}]
    serializer.serialize_contacts(contacts)
    deserialized_contacts = serializer.deserialize_contacts()
    print(deserialized_contacts)