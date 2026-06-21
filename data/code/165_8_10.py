def merge_contacts(contacts1, contacts2):
    contact_set = set()
    for contact in contacts1 + contacts2:
        contact_set.add((contact['name'], contact['phone']))
    return sorted(list(contact_set), key=lambda x: x[0])

if __name__ == '__main__':
    contacts1 = [{'name': 'Alice', 'phone': '1234567890'}, {'name': 'Bob', 'phone': '0987654321'}]
    contacts2 = [{'name': 'Charlie', 'phone': '1122334455'}, {'name': 'Alice', 'phone': '1234567890'}]
    merged_contacts = merge_contacts(contacts1, contacts2)
    print(merged_contacts)