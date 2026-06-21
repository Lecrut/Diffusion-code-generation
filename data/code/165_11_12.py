import operator

def validate_contacts(contacts):
    if not all(isinstance(contact, dict) and 'last_name' in contact for contact in contacts):
        raise ValueError("All items in the list must be dictionaries with a 'last_name' key.")

def sort_contacts_by_last_name(contacts):
    validate_contacts(contacts)
    return sorted(contacts, key=operator.itemgetter('last_name'))

if __name__ == '__main__':
    contacts = [
        {'first_name': 'Robert', 'last_name': 'Brown'},
        {'first_name': 'Emily', 'last_name': 'Davis'},
        {'first_name': 'Michael', 'last_name': 'Wilson'}
    ]
    try:
        sorted_contacts = sort_contacts_by_last_name(contacts)
        print(sorted_contacts)
    except ValueError as e:
        print(e)