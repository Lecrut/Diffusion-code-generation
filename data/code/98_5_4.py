def process_items(data):
    results = []
    for item in data:
        status = "Unknown"
        if item.get('active'):
            status = "Active"
        elif item.get('premium'):
            status = "Premium"
        elif item.get('expired'):
            status = "Expired"
        else:
            status = "Inactive"
        item['status'] = status
        results.append(item)
    return results
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'ItemA', 'active': True, 'premium': False, 'expired': False},
        {'id': 2, 'name': 'ItemB', 'active': False, 'premium': True, 'expired': False},
        {'id': 3, 'name': 'ItemC', 'active': False, 'premium': False, 'expired': True},
        {'id': 4, 'name': 'ItemD', 'active': True, 'premium': True, 'expired': False},
        {'id': 5, 'name': 'ItemE', 'active': False, 'premium': False, 'expired': False}
    ]
    processed_data = process_items(sample_data)
    for item in processed_data:
        print(item)