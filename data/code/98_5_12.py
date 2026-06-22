def classify_items(items):
    results = []
    for item in items:
        classification = _get_classification(item)
        entry = {
            'id': item['id'],
            'name': item['name'],
            'classification': classification
        }
        results.append(entry)
    return results

def _get_classification(item):
    status = item.get('status')
    item_type = item.get('type')
    expiry = item.get('expiry_date')
    
    if status == 'active':
        return 'Active'
    
    if item_type == 'premium':
        return 'Premium'
    
    if expiry is not None and expiry < '2023-01-01':
        return 'Expired'
    
    return 'Standard'

if __name__ == '__main__':
    sample_items = [
        {'id': 1, 'name': 'Alpha', 'status': 'active', 'type': 'standard', 'expiry_date': '2025-05-15'},
        {'id': 2, 'name': 'Beta', 'status': 'inactive', 'type': 'premium', 'expiry_date': '2024-01-01'},
        {'id': 3, 'name': 'Gamma', 'status': 'inactive', 'type': 'standard', 'expiry_date': '2022-12-31'},
        {'id': 4, 'name': 'Delta', 'status': 'inactive', 'type': 'standard', 'expiry_date': '2025-01-01'},
    ]
    output = classify_items(sample_items)
    print(output)