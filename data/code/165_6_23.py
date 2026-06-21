import json

def serialize_contacts(contacts):
    return json.dumps(contacts)

def deserialize_contacts(json_data):
    contacts = json.loads(json_data)
    for contact in contacts:
        contact.setdefault('name', 'Unknown')
        contact.setdefault('phone', 'N/A')
        contact.setdefault('email', 'no-email@example.com')
    return contacts

if __name__ == '__main__':
    sample_contacts = [
        {'name': 'Alice', 'phone': '123-456-7890'},
        {'name': 'Bob', 'email': 'bob@example.com'}
    ]
    
    json_data = serialize_contacts(sample_contacts)
    print(json_data)
    
    deserialized_contacts = deserialize_contacts(json_data)
    print(deserialized_contacts)