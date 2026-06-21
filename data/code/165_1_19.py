from collections import namedtuple

Contact = namedtuple('Contact', ['first_name', 'last_name', 'phone_number'])

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, first_name, last_name, phone_number):
        if not all([first_name, last_name, phone_number]):
            return False
        if not all(isinstance(attr, str) for attr in [first_name, last_name, phone_number]):
            return False
        self.contacts.append(Contact(first_name, last_name, phone_number))
        return True

    def search_by_phone(self, phone_number):
        return [contact for contact in self.contacts if contact.phone_number == phone_number]

    def sort_contacts_by_last_name(self):
        return sorted(self.contacts, key=lambda x: x.last_name)

if __name__ == '__main__':
    manager = ContactManager()
    manager.add_contact('Alice', 'Johnson', '123-456-7890')
    manager.add_contact('Bob', 'Smith', '098-765-4321')
    print(manager.search_by_phone('123-456-7890'))
    print(manager.sort_contacts_by_last_name())