def categorize_item(item):
    if item.get('status') == 'active':
        return 'Active'
    elif item.get('type') == 'premium':
        return 'Premium'
    elif item.get('expiry_date') and item.get('expiry_date') < '2023-01-01':
        return 'Expired'
    else:
        return 'Inactive'

def process_items(items):
    processed_list = []
    for item in items:
        try:
            categorized_status = categorize_item(item)
            item['processed_status'] = categorized_status
            processed_list.append(item)
        except Exception as e:
            print(f'Error processing item {item.get('id')}: {e}')
            processed_list.append(item)
    return processed_list
if __name__ == '__main__':
    sample_data = [{'id': 1, 'name': 'Item A', 'status': 'active', 'type': 'standard', 'expiry_date': '2024-12-31'}, {'id': 2, 'name': 'Item B', 'type': 'premium', 'expiry_date': '2022-12-31'}, {'id': 3, 'name': 'Item C', 'expiry_date': '2023-02-01'}, {'id': 4, 'name': 'Item D'}]
    result = process_items(sample_data)
    for item in result:
        print(item)