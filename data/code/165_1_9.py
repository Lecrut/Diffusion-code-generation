from collections import namedtuple

Contact = namedtuple('Contact', ['first_name', 'last_name', 'phone_number'])

def add_contact(contacts, first_name, last_name, phone_number):
    if not first_name or not last_name or not phone_number:
        return False
    contacts.append(Contact(first_name, last_name, phone_number))
    return True

def search_contact_by_phone(contacts, phone_number):
    for contact in contacts:
        if contact.phone_number == phone_number:
            return contact
    return None

def get_all_contacts_sorted(contacts):
    return sorted(contacts, key=lambda x: x.last_name)

if __name__ == '__main__':
    contacts = []
    add_contact(contacts, 'Alice', 'Johnson', '555-1234')
    add_contact(contacts, 'Bob', 'Smith', '555-5678')
    print(search_contact_by_phone(contacts, '555-1234'))
    sorted_contacts = get_all_contacts_sorted(contacts)
    for contact in sorted_contacts:
        print(f"Name: {contact.first_name} {contact.last_name}, Phone: {contact.phone_number}")