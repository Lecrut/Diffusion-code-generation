import re

def validate_contact(contact):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    phone_pattern = r'^\d{10}$'
    
    if re.match(email_pattern, contact['email']) and re.match(phone_pattern, contact['phone']):
        return True
    return False

def filter_contacts(contacts):
    return [contact for contact in contacts if validate_contact(contact)]

if __name__ == '__main__':
    sample_contacts = [
        {'name': 'John Doe', 'email': 'john.doe@example.com', 'phone': '1234567890'},
        {'name': 'Jane Smith', 'email': 'jane.smith@invalid', 'phone': '123456789'},
        {'name': 'Alice Johnson', 'email': 'alice.johnson@example.com', 'phone': '12345678901'}
    ]
    
    valid_contacts = filter_contacts(sample_contacts)
    print(valid_contacts)