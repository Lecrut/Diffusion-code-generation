import sys
contacts = {}
def add_contact(name, phone, email):
    if not name or not phone or not email:
        print("Error: All fields must be provided.")
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
    if name in contacts:
        del contacts[name]
        return True
    else:
        print(f"Error: Contact '{name}' not found.")
        return False
if __name__ == '__main__':
    print("--- Initializing Contact Book with Sample Data ---")
    add_contact("Alice", "123-456-7890", "alice@example.com")
    add_contact("Bob", "987-654-3210", "bob@example.com")
    add_contact("Charlie", "555-123-4567", "charlie@example.com")
    list_contacts()
    print("\n--- Attempting to Delete Contact ---")
    delete_contact("Bob")
    delete_contact("NonExistent")
    list_contacts()