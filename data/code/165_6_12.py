import json

def serialize_contacts(contacts):
    return json.dumps(contacts, default=lambda o: {'name': '', 'phone': '', 'email': ''}, indent=4)

def deserialize_contacts(json_str):
    return json.loads(json_str, object_hook=lambda d: {k: v for k, v in d.items() if k in ['name', 'phone', 'email']})

if __name__ == '__main__':
    contacts = [
        {'name': 'Alice', 'phone': '1234567890'},
        {'name': 'Bob', 'email': 'bob@example.com'},
        {'phone': '0987654321'}
    ]
    
    json_str = serialize_contacts(contacts)
    print(json_str)
    
    deserialized_contacts = deserialize_contacts(json_str)
    print(deserialized_contacts)