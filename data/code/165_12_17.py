import re
CASE_INSENSITIVE_FLAGS = re.IGNORECASE

class ContactSearch:

    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if not name or not phone or (not email):
            raise ValueError('All fields must be provided.')
        self.contacts[name.lower()] = {'phone': phone, 'email': email}

    def search_contacts(self, query):
        pattern = re.compile(re.escape(query), CASE_INSENSITIVE_FLAGS)
        matching_contacts = {name: details for name, details in self.contacts.items() if pattern.search(name)}
        return matching_contacts

    def list_contacts(self):
        if not self.contacts:
            print('No contacts found.')
            return
        print('\n--- Contact Book ---')
        for name, details in self.contacts.items():
            print(f'Name: {name}, Phone: {details['phone']}, Email: {details['email']}')
        print('--------------------')
if __name__ == '__main__':
    contact_search = ContactSearch()
    contact_search.add_contact('Alice Johnson', '123-456-7890', 'alice@example.com')
    contact_search.add_contact('Bob Smith', '987-654-3210', 'bob@example.com')
    print('\n--- Search Results ---')
    matching_contacts = contact_search.search_contacts('li')
    for name, details in matching_contacts.items():
        print(f'Name: {name}, Phone: {details['phone']}, Email: {details['email']}')
    contact_search.list_contacts()