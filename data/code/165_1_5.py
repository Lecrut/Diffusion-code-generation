from collections import namedtuple

Contact = namedtuple('Contact', ['first_name', 'last_name', 'phone_number'])

def add_contact(contacts, first_name, last_name, phone_number):
    contacts.append(Contact(first_name, last_name, phone_number))

def search_by_phone(contacts, phone_number):
    return [contact for contact in contacts if contact.phone_number == phone_number]

def sort_contacts_by_last_name(contacts):
    return sorted(contacts, key=lambda x: x.last_name)

if __name__ == '__main__':
    contacts = []
    add_contact(contacts, 'John', 'Doe', '123-456-7890')
    add_contact(contacts, 'Jane', 'Smith', '987-654-3210')
    print(search_by_phone(contacts, '123-456-7890'))
    print(sort_contacts_by_last_name(contacts))