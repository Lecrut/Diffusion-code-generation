import json

DEFAULT_CONTACT_FIELDS = {
    'name': '',
    'phone': '',
    'email': ''
}

def serialize_contacts(contacts, filename):
    with open(filename, 'w') as file:
        json.dump([contact | DEFAULT_CONTACT_FIELDS for contact in contacts], file)

def deserialize_contacts(filename):
    with open(filename, 'r') as file:
        return [contact for contact in json.load(file)]

if __name__ == '__main__':
    sample_contacts = [
        {'name': 'Alice', 'phone': '123-456-7890'},
        {'email': 'bob@example.com'}
    ]
    output_filename = 'sample_contacts.json'
    serialize_contacts(sample_contacts, output_filename)
    deserialized_contacts = deserialize_contacts(output_filename)
    print(deserialized_contacts)