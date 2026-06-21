import operator

def sort_contacts_by_last_name(contacts):
    return sorted(contacts, key=operator.itemgetter('last_name'))

if __name__ == '__main__':
    contacts = [
        {'first_name': 'Robert', 'last_name': 'Brown'},
        {'first_name': 'Emily', 'last_name': 'Davis'},
        {'first_name': 'Michael', 'last_name': 'Wilson'}
    ]
    sorted_contacts = sort_contacts_by_last_name(contacts)
    print(sorted_contacts)