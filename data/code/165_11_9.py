import operator

class ContactSorter:
    CONTACT_KEY = 'last_name'

    @staticmethod
    def sort_contacts(contacts):
        return sorted(contacts, key=operator.itemgetter(ContactSorter.CONTACT_KEY))

if __name__ == '__main__':
    contacts = [
        {'first_name': 'John', 'last_name': 'Doe'},
        {'first_name': 'Jane', 'last_name': 'Smith'},
        {'first_name': 'Alice', 'last_name': 'Johnson'}
    ]
    sorted_contacts = ContactSorter.sort_contacts(contacts)
    print(sorted_contacts)