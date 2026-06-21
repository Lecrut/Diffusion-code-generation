import re

def validate_contact(contact):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    phone_pattern = r'^\d{10}$'
    return re.match(email_pattern, contact['email']) and re.match(phone_pattern, contact['phone'])

def filter_contacts(contacts):
    valid_contacts = []
    for contact in contacts:
        if validate_contact(contact):
            valid_contacts.append(contact)
    return valid_contacts

if __name__ == '__main__':
    sample_contacts = [
        {'name': 'Alice', 'email': 'alice@example.com', 'phone': '1234567890'},
        {'name': 'Bob', 'email': 'bob@invalid-email', 'phone': '123456789'},
        {'name': 'Charlie', 'email': 'charlie@example.com', 'phone': '12345678901'}
    ]
    valid_contacts = filter_contacts(sample_contacts)
    print(valid_contacts)