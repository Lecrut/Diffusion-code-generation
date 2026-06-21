from dataclasses import dataclass

@dataclass(frozen=True)
class Contact:
    name: str
    email: str

def deduplicate_contacts(contacts):
    seen_emails = set()
    deduplicated = []
    for contact in contacts:
        if contact.email not in seen_emails:
            seen_emails.add(contact.email)
            deduplicated.append(contact)
    return deduplicated

if __name__ == '__main__':
    raw_contacts = [
        {'name': 'Alice', 'email': 'alice@example.com'},
        {'name': 'Bob', 'email': 'bob@example.com'},
        {'name': 'Alice', 'email': 'alice@example.com'}
    ]
    contacts = [Contact(**contact) for contact in raw_contacts]
    deduplicated_contacts = deduplicate_contacts(contacts)
    print(deduplicated_contacts)