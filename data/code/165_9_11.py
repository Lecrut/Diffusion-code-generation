import re

def validate_contact_info(contacts):
    valid_contacts = []
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    phone_regex = r'^\d{10}$'

    for contact in contacts:
        if re.match(email_regex, contact['email']) and re.match(phone_regex, contact['phone']):
            valid_contacts.append(contact)

    return valid_contacts

if __name__ == '__main__':
    sample_contacts = [
        {'name': 'John Doe', 'email': 'john.doe@example.com', 'phone': '1234567890'},
        {'name': 'Jane Smith', 'email': 'jane.smith@invalid-email', 'phone': '123456789'},
        {'name': 'Alice Johnson', 'email': 'alice.johnson@example.com', 'phone': '12345678901'}
    ]
    print(validate_contact_info(sample_contacts))