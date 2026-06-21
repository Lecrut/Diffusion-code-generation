def merge_contacts(contacts1, contacts2):
    merged_set = set(contacts1) | set(contacts2)
    return sorted(list(merged_set), key=lambda x: x['name'])

if __name__ == '__main__':
    contacts1 = [{'name': 'Alice', 'phone': '1234567890'}, {'name': 'Bob', 'phone': '0987654321'}]
    contacts2 = [{'name': 'Charlie', 'phone': '1122334455'}, {'name': 'Alice', 'phone': '1234567890'}]
    print(merge_contacts(contacts1, contacts2))