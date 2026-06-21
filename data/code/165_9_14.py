import re

def validate_contact(contact):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    phone_pattern = r'^\d{10}$'
    if not re.match(email_pattern, contact['email']):
        raise ValueError("Invalid email format")
    if not re.match(phone_pattern, contact['phone']):
        raise ValueError("Phone number must be exactly 10 digits")

def filter_contacts(contacts):
    return [contact for contact in contacts if validate_contact(contact)]

if __name__ == '__main__':
    sample_contacts = [
        {'name': 'Alice', 'email': 'alice@example.com', 'phone': '1234567890'},
        {'name': 'Bob', 'email': 'bob@.com', 'phone': '123456789'},
        {'name': 'Charlie', 'email': 'charlie@example.co.uk', 'phone': '1234567890'}
    ]
    try:
        valid_contacts = filter_contacts(sample_contacts)
        print(valid_contacts)
    except ValueError as e:
        print(e)