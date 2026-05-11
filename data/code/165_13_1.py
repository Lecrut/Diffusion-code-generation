def find_contact(contacts, name):
    for contact in contacts:
        if contact.get("name") == name:
            return contact
    return None
if __name__ == '__main__':
    sample_contacts = [
        {"name": "Alice", "phone": "111-222-3333", "email": "alice@example.com"},
        {"name": "Bob", "phone": "444-555-6666", "email": "bob@example.com"},
        {"name": "Charlie", "phone": "777-888-9999", "email": "charlie@example.com"}
    ]
    search_name = "Bob"
    result = find_contact(sample_contacts, search_name)
    print(result)
    search_name = "David"
    result = find_contact(sample_contacts, search_name)
    print(result)