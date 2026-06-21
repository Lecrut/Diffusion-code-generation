from collections import namedtuple

Contact = namedtuple('Contact', ['first_name', 'last_name', 'phone_number'])

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, first_name, last_name, phone_number):
        if not first_name or not last_name or not phone_number:
            return False
        if not isinstance(first_name, str) or not isinstance(last_name, str) or not isinstance(phone_number, str):
            return False
        self.contacts.append(Contact(first_name, last_name, phone_number))
        return True

    def search_by_phone(self, phone_number):
        return [contact for contact in self.contacts if contact.phone_number == phone_number]

    def get_all_contacts_sorted(self):
        return sorted(self.contacts, key=lambda x: x.last_name)

if __name__ == '__main__':
    manager = ContactManager()
    success1 = manager.add_contact("Alice", "Smith", "123-456-7890")
    print(f"Attempt to add valid contact: {success1}")
    result1 = manager.search_by_phone("123-456-7890")
    print(f"Search by phone '123-456-7890': {result1}")
    manager.add_contact("Bob", "Johnson", "098-765-4321")
    sorted_contacts = manager.get_all_contacts_sorted()
    print(f"All contacts sorted by last name: {[contact for contact in sorted_contacts]}")