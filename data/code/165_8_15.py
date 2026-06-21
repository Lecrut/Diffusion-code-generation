def merge_contacts(contacts1, contacts2):
    contact_set = set()
    for contact in contacts1:
        contact_set.add((contact['name'], contact['phone']))
    for contact in contacts2:
        contact_set.add((contact['name'], contact['phone']))
    return sorted([{'name': name, 'phone': phone} for name, phone in contact_set], key=lambda x: x['name'])

def main():
    sample_contacts1 = [
        {'name': 'Alice', 'phone': '123-456-7890'},
        {'name': 'Bob', 'phone': '987-654-3210'}
    ]
    sample_contacts2 = [
        {'name': 'Charlie', 'phone': '555-555-5555'},
        {'name': 'Alice', 'phone': '123-456-7890'}
    ]
    merged_contacts = merge_contacts(sample_contacts1, sample_contacts2)
    print(merged_contacts)

if __name__ == '__main__':
    main()