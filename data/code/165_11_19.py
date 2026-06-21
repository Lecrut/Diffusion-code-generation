import operator

def sort_contacts_by_last_name(contacts):
    return sorted(contacts, key=operator.itemgetter('last_name'))

if __name__ == '__main__':
    CONTACTS = [
        {'first_name': 'John', 'last_name': 'Doe'},
        {'first_name': 'Jane', 'last_name': 'Smith'},
        {'first_name': 'Alice', 'last_name': 'Johnson'}
    ]
    sorted_contacts = sort_contacts_by_last_name(CONTACTS)
    print(sorted_contacts)