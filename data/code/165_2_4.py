def search_contacts(contacts, search_name):
    found_contacts = []
    for contact in contacts:
        if search_name.lower() in contact['name'].lower():
            found_contacts.append(contact)
    return found_contacts
contacts_data = [
    {'name': 'Alice Smith', 'phone': '123-456-7890', 'email': 'alice@example.com'},
    {'name': 'Bob Johnson', 'phone': '987-654-3210', 'email': 'bob@example.com'},
    {'name': 'Charlie Brown', 'phone': '555-123-4567', 'email': 'charlie@example.com'},
    {'name': 'David Lee', 'phone': '222-333-4444', 'email': 'david@example.com'}
]
search_term = "Smith"
results = search_contacts(contacts_data, search_term)
if __name__ == '__main__':
    print(f"Searching for contacts containing: {search_term}")
    if results:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts found matching the search term.")