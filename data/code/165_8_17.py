def merge_contacts(contacts1, contacts2):
    combined = set(contacts1 + contacts2)
    return sorted(combined, key=lambda x: x['name'])
if __name__ == '__main__':
    sample_contacts_1 = [{'name': 'Alice', 'phone': '123-456-7890'}, {'name': 'Bob', 'phone': '987-654-3210'}]
    sample_contacts_2 = [{'name': 'Charlie', 'phone': '555-555-5555'}, {'name': 'Alice', 'phone': '123-456-7890'}]
    merged_contacts = merge_contacts(sample_contacts_1, sample_contacts_2)
    print(merged_contacts)