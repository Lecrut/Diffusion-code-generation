import json

class ContactSerializer:
    DEFAULT_NAME = ''
    DEFAULT_PHONE = ''
    DEFAULT_EMAIL = ''

    @staticmethod
    def serialize_contacts(contacts, filename):
        with open(filename, 'w') as file:
            json.dump([{'name': contact.get('name', ContactSerializer.DEFAULT_NAME), 
                        'phone': contact.get('phone', ContactSerializer.DEFAULT_PHONE), 
                        'email': contact.get('email', ContactSerializer.DEFAULT_EMAIL)} 
                       for contact in contacts], file)

    @staticmethod
    def deserialize_contacts(filename):
        with open(filename, 'r') as file:
            return [contact for contact in json.load(file)]

if __name__ == '__main__':
    sample_contacts = [
        {'name': 'Alice', 'phone': '123-456-7890'},
        {'email': 'bob@example.com'}
    ]
    output_filename = 'sample_contacts.json'
    ContactSerializer.serialize_contacts(sample_contacts, output_filename)
    deserialized_contacts = ContactSerializer.deserialize_contacts(output_filename)
    print(deserialized_contacts)