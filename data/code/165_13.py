def find_contact(contacts, name):
    for contact in contacts:
        if contact.get("name") == name:
            return contact
    return None
if __name__ == '__main__':
    sample_contacts = [
        {"id": 1, "name": "Alice", "phone": "111-222-3333"},
        {"id": 2, "name": "Bob", "phone": "444-555-6666"},
        {"id": 3, "name": "Charlie", "phone": "777-888-9999"}
    ]
    search_name = "Bob"
    result = find_contact(sample_contacts, search_name)
    print(result)
    search_name = "David"
    result = find_contact(sample_contacts, search_name)
    print(result)