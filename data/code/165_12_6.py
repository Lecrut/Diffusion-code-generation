import sys
contacts = {}
def add_contact(name, phone, email):
    if not name or not phone or not email:
        print("Error: All fields must be provided.")
        return False
    if name in contacts:
        print(f"Error: Contact '{name}' already exists.")
        return False
    contacts[name] = {"phone": phone, "email": email}
    return True
def list_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact Book ---")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    print("--------------------")
def delete_contact(name):
    if name not in contacts:
        print(f"Error: Contact '{name}' not found.")
        return False
    del contacts[name]
    return True
def main():
    sample_contacts = [
        ("Alice", "123-456-7890", "alice@example.com"),
        ("Bob", "987-654-3210", "bob@example.com"),
        ("Charlie", "555-123-4567", "charlie@example.com")
    ]
    for name, phone, email in sample_contacts:
        add_contact(name, phone, email)
    list_contacts()
    print("\n--- Deleting Sample Contact (Bob) ---")
    delete_contact("Bob")
    list_contacts()
    print("\n--- Attempting to delete non-existent contact (David) ---")
    delete_contact("David")
    list_contacts()
if __name__ == '__main__':
    main()