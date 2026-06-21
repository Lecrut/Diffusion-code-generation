import json

def serialize_contacts(contacts, filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file)

def deserialize_contacts(filename):
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == '__main__':
    contacts = [
        {'name': 'Alice', 'phone': '1234567890'},
        {'name': 'Bob', 'email': 'bob@example.com'}
    ]
    filename = 'contacts.json'
    
    serialize_contacts(contacts, filename)
    deserialized_contacts = deserialize_contacts(filename)
    
    print(deserialized_contacts)