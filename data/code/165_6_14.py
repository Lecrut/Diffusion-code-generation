import json

class ContactSerializer:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name='', phone='', email=''):
        contact = {
            'name': name,
            'phone': phone,
            'email': email
        }
        self.contacts.append(contact)

    def serialize_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    @staticmethod
    def deserialize_from_file(filename):
        with open(filename, 'r') as file:
            return json.load(file)

if __name__ == '__main__':
    serializer = ContactSerializer()
    serializer.add_contact(name='Alice', phone='123-456-7890')
    serializer.add_contact(email='bob@example.com')
    filename = 'contacts.json'
    serializer.serialize_to_file(filename)
    deserialized_contacts = serializer.deserialize_from_file(filename)
    print(deserialized_contacts)