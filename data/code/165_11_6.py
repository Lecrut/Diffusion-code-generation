import operator

def sort_contacts_by_last_name(contacts):
    if not all(isinstance(contact, dict) and 'last_name' in contact for contact in contacts):
        raise ValueError("All items in the list must be dictionaries with a 'last_name' key.")
    
    return sorted(contacts, key=operator.itemgetter('last_name'))

if __name__ == '__main__':
    contacts = [
        {'first_name': 'John', 'last_name': 'Doe'},
        {'first_name': 'Jane', 'last_name': 'Smith'},
        {'first_name': 'Alice', 'last_name': 'Johnson'}
    ]
    
    try:
        sorted_contacts = sort_contacts_by_last_name(contacts)
        print(sorted_contacts)
    except ValueError as e:
        print(e)