import json
import os
class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = []
        self.load()
    def load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.contacts = json.load(f)
            except json.JSONDecodeError:
                self.contacts = []
        else:
            self.contacts = []
    def save(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.contacts, f, indent=4)
        except IOError:
            pass
    def add_contact(self, name, phone, email):
        self.contacts.append({"name": name, "phone": phone, "email": email})
def main():
    book = ContactBook()
    book.add_contact("Alice", "123-456-7890", "alice@example.com")
    book.add_contact("Bob", "987-654-3210", "bob@example.com")
    book.add_contact("Charlie", "555-123-4567", "charlie@example.com")
    print("--- Contact Book Loaded ---")
    for contact in book.contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print("\n--- Program Exiting, Saving Data ---")
    book.save()
    print("Data saved successfully to contacts.json")
if __name__ == '__main__':
    main()