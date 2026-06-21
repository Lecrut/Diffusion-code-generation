import re

def validate_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None

def validate_phone(phone):
    phone_pattern = r'^\d{10}$'
    return re.match(phone_pattern, phone) is not None

def filter_contacts(contacts):
    return [contact for contact in contacts if validate_email(contact['email']) and validate_phone(contact['phone'])]

if __name__ == '__main__':
    sample_contacts = [
        {'name': 'Alice', 'email': 'alice@example.com', 'phone': '1234567890'},
        {'name': 'Bob', 'email': 'bob@.com', 'phone': '123456789'},
        {'name': 'Charlie', 'email': 'charlie@example.co.uk', 'phone': '1234567890'}
    ]
    valid_contacts = filter_contacts(sample_contacts)
    print(valid_contacts)