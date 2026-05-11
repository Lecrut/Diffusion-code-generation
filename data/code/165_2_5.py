def search_contacts(contacts, search_name):
    found_contacts = []
    for contact in contacts:
        if search_name.lower() in contact['name'].lower():
            found_contacts.append(contact)
    return found_contacts
if __name__ == '__main__':
    sample_contacts = [
        {'name': 'Alice Smith', 'phone': '123-456-7890', 'email': 'alice@example.com'},
        {'name': 'Bob Johnson', 'phone': '987-654-3210', 'email': 'bob@example.com'},
        {'name': 'Charlie Brown', 'phone': '555-123-4567', 'email': 'charlie@example.com'},
        {'name': 'Alice Williams', 'phone': '111-222-3333', 'email': 'alice.w@example.com'}
    ]
    search_term = "Alice"
    results = search_contacts(sample_contacts, search_term)
    if results:
        print(f"Contacts found for '{search_term}':")
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print(f"No contacts found matching '{search_term}'.")
    search_term_2 = "Bob"
    results_2 = search_contacts(sample_contacts, search_term_2)
    if results_2:
        print(f"\nContacts found for '{search_term_2}':")
        for contact in results_2:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print(f"\nNo contacts found matching '{search_term_2}'.")