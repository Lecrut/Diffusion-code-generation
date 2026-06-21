import json

DEFAULT_VALUES = {
    'name': '',
    'phone': '',
    'email': ''
}

def serialize_contacts(contacts, filename):
    formatted_contacts = [{key: contact.get(key, DEFAULT_VALUES[key]) for key in DEFAULT_VALUES} for contact in contacts]
    with open(filename, 'w') as file:
        json.dump(formatted_contacts, file)

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