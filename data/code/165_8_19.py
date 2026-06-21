def merge_contacts(contacts1, contacts2):
    contact_set = set()
    for contact in contacts1 + contacts2:
        if contact['phone'] not in contact_set:
            contact_set.add(contact['phone'])
            yield contact

if __name__ == '__main__':
    contacts1 = [{'name': 'Alice', 'phone': '123'}, {'name': 'Bob', 'phone': '456'}]
    contacts2 = [{'name': 'Charlie', 'phone': '789'}, {'name': 'Alice', 'phone': '123'}]
    merged_contacts = list(merge_contacts(contacts1, contacts2))
    for contact in sorted(merged_contacts, key=lambda x: x['name']):
        print(contact)