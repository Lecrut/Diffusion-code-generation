import json

def serialize_contacts(contacts, filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file)

def deserialize_contacts(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def fill_defaults(contact):
    defaults = {'name': '', 'phone': '', 'email': ''}
    return {**defaults, **contact}

if __name__ == '__main__':
    contacts = [
        {'name': 'Alice', 'phone': '123-456-7890'},
        {'email': 'bob@example.com'}
    ]
    filename = 'contacts.json'
    
    serialize_contacts(contacts, filename)
    loaded_contacts = deserialize_contacts(filename)
    
    filled_contacts = [fill_defaults(contact) for contact in loaded_contacts]
    print(filled_contacts)