class ContactBook:
    def __init__(self, filename="contacts.txt"):
        self.filename = filename
        self.contacts = []
    def add_contact(self, name, phone, email):
        new_contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(new_contact)
        self.save_contacts()
    def display_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
            return
        print("\n--- Contact List ---")
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print("--------------------")
    def save_contacts(self):
        with open(self.filename, "w") as f:
            for contact in self.contacts:
                f.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")
    def load_contacts(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        name, phone, email = parts
                        self.contacts.append({"name": name, "phone": phone, "email": email})
        except FileNotFoundError:
            pass
if __name__ == '__main__':
    book = ContactBook("sample_contacts.txt")
    book.add_contact("Alice Smith", "123-456-7890", "alice@example.com")
    book.add_contact("Bob Johnson", "987-654-3210", "bob@example.com")
    book.add_contact("Charlie Brown", "555-123-4567", "charlie@example.com")
    book.display_contacts()
    book.load_contacts()
    print("\n--- Loaded Contacts ---")
    book.display_contacts()