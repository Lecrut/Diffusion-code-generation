from dataclasses import dataclass

@dataclass(frozen=True)
class Contact:
    name: str
    email: str

def deduplicate_contacts(contacts):
    seen_emails = set()
    unique_contacts = []
    for contact in contacts:
        if contact.email not in seen_emails:
            seen_emails.add(contact.email)
            unique_contacts.append(contact)
    return unique_contacts

if __name__ == '__main__':
    raw_contacts = [
        {'name': 'Alice', 'email': 'alice@example.com'},
        {'name': 'Bob', 'email': 'bob@example.com'},
        {'name': 'Alice', 'email': 'alice@example.com'}
    ]
    contacts = [Contact(**contact) for contact in raw_contacts]
    unique_contacts = deduplicate_contacts(contacts)
    print(unique_contacts)