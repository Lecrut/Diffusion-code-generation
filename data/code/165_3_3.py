def display_contact_book(contacts):
    print("--- Contact Book ---")
    if not contacts:
        print("The contact book is empty.")
        return
    for index, contact in enumerate(contacts):
        print(f"\nContact {index + 1}:")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
if __name__ == '__main__':
    sample_contacts = [
        {'name': 'Alice Smith', 'phone': '123-456-7890', 'email': 'alice@example.com'},
        {'name': 'Bob Johnson', 'phone': '987-654-3210', 'email': 'bob@example.com'},
        {'name': 'Charlie Brown', 'phone': '555-123-4567', 'email': 'charlie@example.com'}
    ]
    display_contact_book(sample_contacts)