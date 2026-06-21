def merge_contacts(contacts1, contacts2):
    contact_set = set()
    for contact in contacts1 + contacts2:
        contact_set.add((contact['name'], contact['phone']))
    return sorted([{'name': name, 'phone': phone} for name, phone in contact_set], key=lambda x: x['name'])

if __name__ == '__main__':
    contacts1 = [{'name': 'Alice', 'phone': '123'}, {'name': 'Bob', 'phone': '456'}]
    contacts2 = [{'name': 'Charlie', 'phone': '789'}, {'name': 'Alice', 'phone': '123'}]
    print(merge_contacts(contacts1, contacts2))