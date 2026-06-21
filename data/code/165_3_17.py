from dataclasses import dataclass

@dataclass(frozen=True)
class Contact:
    name: str
    phone: str
    email: str

def deduplicate_contacts(contacts):
    seen_emails = set()
    deduplicated = []
    for contact in contacts:
        if contact['email'] not in seen_emails:
            seen_emails.add(contact['email'])
            deduplicated.append(Contact(**contact))
    return deduplicated

if __name__ == '__main__':
    sample_contacts = [
        {'name': 'Alice Smith', 'phone': '123-456-7890', 'email': 'alice@example.com'},
        {'name': 'Bob Johnson', 'phone': '987-654-3210', 'email': 'bob@example.com'},
        {'name': 'Charlie Brown', 'phone': '555-123-4567', 'email': 'charlie@example.com'},
        {'name': 'Alice Smith', 'phone': '987-654-3210', 'email': 'alice@example.com'}
    ]
    deduplicated_contacts = deduplicate_contacts(sample_contacts)
    for contact in deduplicated_contacts:
        print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")