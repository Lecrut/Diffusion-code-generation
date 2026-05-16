def process_items(items):
    processed_list = []
    for item in items:
        result = None
        if item.get('status') == 'active':
            result = "Active"
        elif item.get('type') == 'premium':
            result = "Premium"
        elif item.get('expiry_date') and item.get('expiry_date') < '2023-01-01':
            result = "Expired"
        else:
            result = "Inactive"
        item['processed_status'] = result
        processed_list.append(item)
    return processed_list
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Item A', 'status': 'active', 'type': 'standard', 'expiry_date': '2024-12-31'},
        {'id': 2, 'name': 'Item B', 'status': 'inactive', 'type': 'premium', 'expiry_date': '2025-01-01'},
        {'id': 3, 'name': 'Item C', 'status': 'active', 'type': 'standard', 'expiry_date': '2022-10-15'},
        {'id': 4, 'name': 'Item D', 'status': 'active', 'type': 'standard', 'expiry_date': '2023-05-20'},
        {'id': 5, 'name': 'Item E', 'status': 'active', 'type': 'premium', 'expiry_date': '2024-01-01'},
        {'id': 6, 'name': 'Item F', 'status': 'active', 'type': 'standard', 'expiry_date': '2021-11-01'},
    ]
    result = process_items(sample_data)
    for item in result:
        print(item)