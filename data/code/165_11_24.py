import operator

class ContactSorter:
    def __init__(self, contacts):
        self.contacts = contacts

    def sort_contacts_by_last_name(self):
        return sorted(self.contacts, key=operator.itemgetter('last_name'))

if __name__ == '__main__':
    contacts = [
        {'first_name': 'John', 'last_name': 'Doe'},
        {'first_name': 'Jane', 'last_name': 'Smith'},
        {'first_name': 'Alice', 'last_name': 'Johnson'}
    ]
    sorter = ContactSorter(contacts)
    sorted_contacts = sorter.sort_contacts_by_last_name()
    print(sorted_contacts)