def validate_items(items):
    if not isinstance(items, list):
        raise ValueError("Input must be a list of items.")
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("Each item must be a dictionary.")

def process_item(item):
    status = None
    if item.get('status') == 'active':
        status = 'Active'
    elif item.get('type') == 'premium':
        status = 'Premium'
    elif item.get('expiry_date') and item.get('expiry_date') < '2023-01-01':
        status = 'Expired'
    else:
        status = 'Inactive'
    return {**item, 'processed_status': status}

def process_items(items):
    validate_items(items)
    processed_list = [process_item(item) for item in items]
    return processed_list

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Item A', 'status': 'active', 'type': 'standard', 'expiry_date': '2024-12-31'},
        {'id': 2, 'name': 'Item B', 'status': 'inactive', 'type': 'premium', 'expiry_date': '2022-12-31'}
    ]
    print(process_items(sample_data))