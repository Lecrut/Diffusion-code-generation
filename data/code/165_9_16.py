import re

class ContactValidator:
    EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    PHONE_PATTERN = r'^\d{10}$'

    @staticmethod
    def validate_contact(contact):
        if re.match(ContactValidator.EMAIL_PATTERN, contact['email']) and re.match(ContactValidator.PHONE_PATTERN, contact['phone']):
            return True
        return False

    @staticmethod
    def filter_contacts(contacts):
        return [contact for contact in contacts if ContactValidator.validate_contact(contact)]

if __name__ == '__main__':
    sample_contacts = [
        {'name': 'Alice', 'email': 'alice@example.com', 'phone': '1234567890'},
        {'name': 'Bob', 'email': 'bob@.com', 'phone': '123456789'},
        {'name': 'Charlie', 'email': 'charlie@example.co.uk', 'phone': '1234567890'}
    ]
    valid_contacts = ContactValidator.filter_contacts(sample_contacts)
    print(valid_contacts)