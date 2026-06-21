import json

def serialize_contacts(contacts, filename):
    with open(filename, 'w') as file:
        json.dump([{'name': contact.get('name', ''), 'phone': contact.get('phone', ''), 'email': contact.get('email', '')} for contact in contacts], file)

def deserialize_contacts(filename):
    try:
        with open(filename, 'r') as file:
            return [contact for contact in json.load(file)]
    except FileNotFoundError:
        print("File not found.")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return []

if __name__ == '__main__':
    contacts = [{'name': 'Alice', 'phone': '1234567890'}, {'email': 'bob@example.com'}]
    filename = 'contacts.json'
    serialize_contacts(contacts, filename)
    deserialized_contacts = deserialize_contacts(filename)
    print(deserialized_contacts)