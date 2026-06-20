STATUS_ACTIVE = 'active'
TYPE_PREMIUM = 'premium'
EXPIRY_THRESHOLD = '2023-01-01'

def process_items(items):
    processed_list = []
    for item in items:
        if item.get('status') == STATUS_ACTIVE:
            result = 'Active'
        elif item.get('type') == TYPE_PREMIUM:
            result = 'Premium'
        elif item.get('expiry_date') and item.get('expiry_date') < EXPIRY_THRESHOLD:
            result = 'Expired'
        else:
            result = 'Inactive'
        item['processed_status'] = result
        processed_list.append(item)
    return processed_list

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Item A', 'status': STATUS_ACTIVE, 'type': 'standard', 'expiry_date': '2024-12-31'},
        {'id': 2, 'name': 'Item B', 'status': 'inactive', 'type': TYPE_PREMIUM, 'expiry_date': '2022-12-31'},
        {'id': 3, 'name': 'Item C', 'status': STATUS_ACTIVE, 'type': 'standard', 'expiry_date': EXPIRY_THRESHOLD},
    ]
    processed_data = process_items(sample_data)
    print(processed_data)