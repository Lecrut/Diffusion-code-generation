from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Contact:
    name: str
    email: str
    phone: str

def deduplicate_contacts(contacts: List[dict]) -> List[Contact]:
    seen_emails = set()
    unique_contacts = []
    for contact in contacts:
        if contact['email'] not in seen_emails:
            seen_emails.add(contact['email'])
            unique_contacts.append(Contact(**contact))
    return unique_contacts

if __name__ == '__main__':
    sample_contacts = [
        {'name': 'Alice', 'email': 'alice@example.com', 'phone': '123-456-7890'},
        {'name': 'Bob', 'email': 'bob@example.com', 'phone': '098-765-4321'},
        {'name': 'Alice', 'email': 'alice@example.com', 'phone': '111-222-3333'}
    ]
    deduplicated_contacts = deduplicate_contacts(sample_contacts)
    for contact in deduplicated_contacts:
        print(contact)