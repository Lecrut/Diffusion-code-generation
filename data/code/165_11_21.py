import operator

class ContactSorter:
    def __init__(self, contacts):
        self.contacts = contacts
    
    def sort_by_last_name(self):
        return sorted(self.contacts, key=operator.itemgetter('last_name'))
    
    def validate_contacts(self):
        if not all(isinstance(contact, dict) and 'last_name' in contact for contact in self.contacts):
            raise ValueError("All items in the list must be dictionaries with a 'last_name' key.")

if __name__ == '__main__':
    contacts = [
        {'first_name': 'Robert', 'last_name': 'Brown'},
        {'first_name': 'Emily', 'last_name': 'Davis'},
        {'first_name': 'Michael', 'last_name': 'Wilson'}
    ]
    
    sorter = ContactSorter(contacts)
    try:
        sorter.validate_contacts()
        sorted_contacts = sorter.sort_by_last_name()
        print(sorted_contacts)
    except ValueError as e:
        print(e)