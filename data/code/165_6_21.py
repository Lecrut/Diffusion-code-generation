import json

def serialize_contacts(contacts, filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file)

def deserialize_contacts(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    contacts = [
        {'name': 'Alice', 'phone': '123-456-7890'},
        {'name': 'Bob', 'email': 'bob@example.com'},
        {'phone': '987-654-3210'}
    ]
    filename = 'contacts.json'
    
    serialize_contacts(contacts, filename)
    deserialized_contacts = deserialize_contacts(filename)
    
    print(deserialized_contacts)

if __name__ == '__main__':
    main()