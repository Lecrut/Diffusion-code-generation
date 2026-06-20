def categorize_items(items):
    categorized_items = []
    for item in items:
        category = None
        if item.get('is_active'):
            category = 'Active'
        elif item.get('is_premium'):
            category = 'Premium'
        elif item.get('expiry_date') and item['expiry_date'] < '2023-01-01':
            category = 'Expired'
        else:
            category = 'Inactive'
        categorized_items.append({'id': item['id'], 'name': item['name'], 'category': category})
    return categorized_items

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Item A', 'is_active': True, 'is_premium': False, 'expiry_date': None},
        {'id': 2, 'name': 'Item B', 'is_active': False, 'is_premium': True, 'expiry_date': '2022-12-31'},
        {'id': 3, 'name': 'Item C', 'is_active': True, 'is_premium': True, 'expiry_date': None},
        {'id': 4, 'name': 'Item D', 'is_active': False, 'is_premium': False, 'expiry_date': '2021-06-30'}
    ]
    result = categorize_items(sample_data)
    print(result)