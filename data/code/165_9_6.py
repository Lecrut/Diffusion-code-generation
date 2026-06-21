import re

class ContactValidator:
    def __init__(self):
        self.email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.phone_pattern = r'^\d{10}$'

    def validate_contact(self, contact):
        if re.match(self.email_pattern, contact['email']) and re.match(self.phone_pattern, contact['phone']):
            return True
        return False

    def filter_contacts(self, contacts):
        return [contact for contact in contacts if self.validate_contact(contact)]

if __name__ == '__main__':
    validator = ContactValidator()
    sample_contacts = [
        {'name': 'Alice', 'email': 'alice@example.com', 'phone': '1234567890'},
        {'name': 'Bob', 'email': 'bob@.com', 'phone': '123456789'},
        {'name': 'Charlie', 'email': 'charlie@example.co.uk', 'phone': '1234567890'}
    ]
    valid_contacts = validator.filter_contacts(sample_contacts)
    print(valid_contacts)