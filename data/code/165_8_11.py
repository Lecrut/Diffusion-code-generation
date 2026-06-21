def merge_contacts(contacts1, contacts2):
    contact_set = set()
    for contact in contacts1 + contacts2:
        if contact['phone'] not in contact_set:
            contact_set.add(contact['phone'])
            yield contact

def main():
    sample_contacts_1 = [{'name': 'Alice', 'phone': '1234567890'}, {'name': 'Bob', 'phone': '0987654321'}]
    sample_contacts_2 = [{'name': 'Charlie', 'phone': '1122334455'}, {'name': 'Alice', 'phone': '1234567890'}]
    merged_contacts = list(merge_contacts(sample_contacts_1, sample_contacts_2))
    sorted_merged_contacts = sorted(merged_contacts, key=lambda x: x['name'])
    for contact in sorted_merged_contacts:
        print(f'Name: {contact['name']}, Phone: {contact['phone']}')
if __name__ == '__main__':
    main()