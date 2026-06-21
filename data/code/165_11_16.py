import operator

class ContactSorter:
    def __init__(self, contacts):
        self.contacts = contacts

    def sort_by_last_name(self):
        return sorted(self.contacts, key=operator.itemgetter('last_name'))

if __name__ == '__main__':
    sorter = ContactSorter([
        {'first_name': 'John', 'last_name': 'Doe'},
        {'first_name': 'Jane', 'last_name': 'Smith'},
        {'first_name': 'Alice', 'last_name': 'Johnson'}
    ])
    sorted_contacts = sorter.sort_by_last_name()
    print(sorted_contacts)