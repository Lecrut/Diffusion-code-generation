from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class Contact:
    name: str
    phone: str
    email: str

def validate_contacts(contacts):
    if not all(isinstance(contact, dict) and 'name' in contact and 'phone' in contact and 'email' in contact for contact in contacts):
        raise ValueError("All contacts must be dictionaries with 'name', 'phone', and 'email' keys.")

def deduplicate_contacts(contacts: List[dict]) -> List[Contact]:
    validate_contacts(contacts)
    email_set = set()
    unique_contacts = []
    for contact in contacts:
        if contact['email'] not in email_set:
            email_set.add(contact['email'])
            unique_contacts.append(Contact(**contact))
    return unique_contacts

if __name__ == '__main__':
    sample_contacts = [
        {'name': 'Alice Smith', 'phone': '123-456-7890', 'email': 'alice@example.com'},
        {'name': 'Bob Johnson', 'phone': '987-654-3210', 'email': 'bob@example.com'},
        {'name': 'Charlie Brown', 'phone': '555-123-4567', 'email': 'charlie@example.com'},
        {'name': 'Alice Smith', 'phone': '123-456-7890', 'email': 'alice@example.com'}
    ]
    unique_contacts = deduplicate_contacts(sample_contacts)
    for contact in unique_contacts:
        print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")