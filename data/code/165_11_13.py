import operator

class ContactSorter:
    CONTACT_KEY = 'last_name'

    @staticmethod
    def validate_contacts(contacts):
        if not all(isinstance(contact, dict) and ContactSorter.CONTACT_KEY in contact for contact in contacts):
            raise ValueError("All items in the list must be dictionaries with a '{}' key.".format(ContactSorter.CONTACT_KEY))

    @classmethod
    def sort_contacts(cls, contacts):
        cls.validate_contacts(contacts)
        return sorted(contacts, key=operator.itemgetter(cls.CONTACT_KEY))

if __name__ == '__main__':
    contacts = [
        {'first_name': 'Robert', 'last_name': 'Brown'},
        {'first_name': 'Emily', 'last_name': 'Davis'},
        {'first_name': 'Michael', 'last_name': 'Wilson'}
    ]
    try:
        sorted_contacts = ContactSorter.sort_contacts(contacts)
        print(sorted_contacts)
    except ValueError as e:
        print(e)