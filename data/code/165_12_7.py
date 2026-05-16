import sys
contacts = []
def add_contact(name, phone, email):
    if not name or not phone or not email:
        print("Error: All fields must be provided.")
        return False
    contacts.append((name, phone, email))
    return True
def list_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact Book ---")
    for i, (name, phone, email) in enumerate(contacts):
        print(f"[{i+1}] Name: {name}, Phone: {phone}, Email: {email}")
    print("--------------------")
def delete_contact(index):
    if not (0 <= index < len(contacts)):
        print("Error: Invalid contact number.")
        return False
    del contacts[index]
    return True
def main():
    sample_contacts = [
        ("Alice", "123-456-7890", "alice@example.com"),
        ("Bob", "987-654-3210", "bob@example.com"),
        ("Charlie", "555-123-4567", "charlie@example.com")
    ]
    contacts.extend(sample_contacts)
    print("--- Contact Book CLI Simulation ---")
    print("\n--- Listing all contacts ---")
    list_contacts()
    print("\n--- Adding new contacts (Sample Data) ---")
    new_contact1 = ("David", "111-222-3333", "david@example.com")
    if add_contact(*new_contact1):
        print(f"Successfully added: {new_contact1[0]}")
    else:
        print("Failed to add contact 1.")
    new_contact2 = ("Eve", "444-555-6666", "eve@example.com")
    if add_contact(*new_contact2):
        print(f"Successfully added: {new_contact2[0]}")
    else:
        print("Failed to add contact 2.")
    print("\n--- Listing all contacts after additions ---")
    list_contacts()
    print("\n--- Deleting a contact (Sample Data) ---")
    if len(contacts) > 0:
        contact_to_delete_index = 0
        print(f"Attempting to delete contact at index {contact_to_delete_index} (Alice)...")
        if delete_contact(contact_to_delete_index):
            print("Deletion successful.")
        else:
            print("Deletion failed.")
    else:
        print("No contacts to delete.")
    print("\n--- Final Contact List ---")
    list_contacts()
if __name__ == '__main__':
    main()