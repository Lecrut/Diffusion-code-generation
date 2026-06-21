import operator

class ContactSorter:
    @staticmethod
    def sort_contacts_by_last_name(contacts):
        return sorted(contacts, key=operator.itemgetter('last_name'))

if __name__ == '__main__':
    contacts = [
        {'first_name': 'John', 'last_name': 'Doe'},
        {'first_name': 'Jane', 'last_name': 'Smith'},
        {'first_name': 'Alice', 'last_name': 'Johnson'}
    ]
    sorted_contacts = ContactSorter.sort_contacts_by_last_name(contacts)
    print(sorted_contacts)