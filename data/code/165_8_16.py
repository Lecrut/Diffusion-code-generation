def merge_contacts(contacts1, contacts2):
    contact_set = set()
    for contact in contacts1 + contacts2:
        if contact['phone'] not in contact_set:
            contact_set.add(contact['phone'])
            yield contact

if __name__ == '__main__':
    contacts_list1 = [{'name': 'Alice', 'phone': '123-456-7890'}, {'name': 'Bob', 'phone': '987-654-3210'}]
    contacts_list2 = [{'name': 'Charlie', 'phone': '555-555-5555'}, {'name': 'Alice', 'phone': '123-456-7890'}]
    merged_contacts = list(merge_contacts(contacts_list1, contacts_list2))
    for contact in sorted(merged_contacts, key=lambda x: x['name']):
        print(contact)