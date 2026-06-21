import json

def validate_contacts(contacts):
    for contact in contacts:
        if 'name' not in contact:
            contact['name'] = ''
        if 'phone' not in contact:
            contact['phone'] = ''
        if 'email' not in contact:
            contact['email'] = ''

def serialize_contacts(contacts, filename):
    validate_contacts(contacts)
    with open(filename, 'w') as file:
        json.dump(contacts, file)

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