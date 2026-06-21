from dataclasses import dataclass

@dataclass
class Contact:
    name: str
    phone: str
    email: str

def deduplicate_contacts(contacts):
    seen_emails = set()
    unique_contacts = []

    for contact in contacts:
        if contact['email'] not in seen_emails:
            seen_emails.add(contact['email'])
            unique_contacts.append(Contact(**contact))

    return unique_contacts

if __name__ == '__main__':
    sample_contacts = [
        {'name': 'Alice Smith', 'phone': '123-456-7890', 'email': 'alice@example.com'},
        {'name': 'Bob Johnson', 'phone': '987-654-3210', 'email': 'bob@example.com'},
        {'name': 'Charlie Brown', 'phone': '555-123-4567', 'email': 'charlie@example.com'},
        {'name': 'Alice Smith', 'phone': '987-654-3210', 'email': 'alice@example.com'}
    ]

    unique_contacts = deduplicate_contacts(sample_contacts)
    for contact in unique_contacts:
        print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")