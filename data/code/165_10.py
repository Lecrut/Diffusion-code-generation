import json
import os
class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = []
        self.load_contacts()
    def load_contacts(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.contacts = json.load(f)
            except json.JSONDecodeError:
                self.contacts = []
        else:
            self.contacts = []
    def save_contacts(self):
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=4)
    def add_contact(self, name, phone, email):
        new_contact = {
            "name": name,
            "phone": phone,
            "email": email
        }
        self.contacts.append(new_contact)
        self.save_contacts()
    def view_all_contacts(self):
        return self.contacts
    def search_contacts(self, query):
        query = query.lower()
        return [contact for contact in self.contacts if query in contact['name'].lower() or query in contact['phone'].lower()]
    def delete_contact(self, name):
        initial_count = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if contact['name'] != name]
        if len(self.contacts) < initial_count:
            self.save_contacts()
            return True
        return False
if __name__ == '__main__':
    book = ContactBook()
    print("--- Initial Contacts ---")
    print(json.dumps(book.view_all_contacts(), indent=2))
    print("\n--- Adding Sample Contacts ---")
    book.add_contact("Alice Smith", "123-456-7890", "alice@example.com")
    book.add_contact("Bob Johnson", "987-654-3210", "bob@example.com")
    book.add_contact("Charlie Brown", "555-123-4567", "charlie@example.com")
    print("\n--- Viewing All Contacts ---")
    all_contacts = book.view_all_contacts()
    print(json.dumps(all_contacts, indent=2))
    print("\n--- Searching for 'Bob' ---")
    search_results_bob = book.search_contacts("Bob")
    print(json.dumps(search_results_bob, indent=2))
    print("\n--- Searching for '123' (Phone Search) ---")
    search_results_123 = book.search_contacts("123")
    print(json.dumps(search_results_123, indent=2))
    print("\n--- Deleting Contact: Alice Smith ---")
    deleted = book.delete_contact("Alice Smith")
    if deleted:
        print("Deletion successful.")
    else:
        print("Contact not found.")
    print("\n--- Viewing Contacts After Deletion ---")
    final_contacts = book.view_all_contacts()
    print(json.dumps(final_contacts, indent=2))