def search_contacts(contacts, search_name):
    found_contacts = []
    for contact in contacts:
        if search_name.lower() in contact['name'].lower():
            found_contacts.append(contact)
    return found_contacts
contacts_data = [
    {"name": "Alice Smith", "phone": "123-456-7890"},
    {"name": "Bob Johnson", "phone": "987-654-3210"},
    {"name": "Charlie Brown", "phone": "555-123-4567"},
    {"name": "Alice Williams", "phone": "111-222-3333"}
]
search_term = "Alice"
results = search_contacts(contacts_data, search_term)
for contact in results:
    print(f"Name: {contact['name']}, Phone: {contact['phone']}")
if __name__ == '__main__':
    pass