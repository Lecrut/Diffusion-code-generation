def display_contact_book(contacts):
    print("--- Contact Book ---")
    if not contacts:
        print("The contact book is empty.")
        return
    for index, contact in enumerate(contacts):
        print(f"\nContact {index + 1}:")
        print(f"Name: {contact.get('name', 'N/A')}")
        print(f"Phone: {contact.get('phone', 'N/A')}")
        print(f"Email: {contact.get('email', 'N/A')}")
if __name__ == '__main__':
    sample_contacts = [
        {"name": "Alice Smith", "phone": "123-456-7890", "email": "alice@example.com"},
        {"name": "Bob Johnson", "phone": "987-654-3210", "email": "bob@example.com"},
        {"name": "Charlie Brown", "phone": "555-123-4567", "email": "charlie@example.com"}
    ]
    display_contact_book(sample_contacts)