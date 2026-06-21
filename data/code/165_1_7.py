from collections import namedtuple

Contact = namedtuple('Contact', ['first_name', 'last_name', 'phone_number'])

class ContactManager:
    def __init__(self):
        self.contacts = []

    @staticmethod
    def validate_contact(name, phone):
        return name and phone and isinstance(name, str) and isinstance(phone, str)

    def add_contact(self, first_name, last_name, phone_number):
        if not self.validate_contact(first_name, phone_number):
            return False
        self.contacts.append(Contact(first_name, last_name, phone_number))
        return True

    def search_by_phone(self, phone_number):
        return [contact for contact in self.contacts if contact.phone_number == phone_number]

    def sort_contacts_by_last_name(self):
        return sorted(self.contacts, key=lambda x: x.last_name)

if __name__ == '__main__':
    manager = ContactManager()
    success1 = manager.add_contact("Alice", "Smith", "123-456-7890")
    print(f"Attempt to add valid contact: {success1}")
    contacts = manager.sort_contacts_by_last_name()
    for contact in contacts:
        print(f"Name='{contact.first_name} {contact.last_name}', Phone='{contact.phone_number}'")