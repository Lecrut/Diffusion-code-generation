from collections import namedtuple

Contact = namedtuple('Contact', ['first_name', 'last_name', 'phone_number'])

def add_contact(contacts, first_name, last_name, phone_number):
    contacts.append(Contact(first_name, last_name, phone_number))

def search_contact_by_phone(contacts, phone_number):
    for contact in contacts:
        if contact.phone_number == phone_number:
            return contact
    return None

def get_all_contacts_sorted(contacts):
    return sorted(contacts, key=lambda x: x.last_name)

if __name__ == '__main__':
    contacts = []
    add_contact(contacts, 'John', 'Doe', '123-456-7890')
    add_contact(contacts, 'Jane', 'Smith', '098-765-4321')
    print(search_contact_by_phone(contacts, '123-456-7890'))
    print(get_all_contacts_sorted(contacts))