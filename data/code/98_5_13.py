def categorize_objects(objects):
    status_map = {
        'active': 'Active',
        'premium': 'Premium',
        'expired': 'Expired',
    }
    results = []
    for obj in objects:
        key = obj.get('type', 'default')
        value = status_map.get(key, 'Unknown')
        if key == 'premium' and obj.get('level', 0) > 5:
            value = 'Super Premium'
        results.append({
            'id': obj.get('id'),
            'category': value
        })
    return results

if __name__ == '__main__':
    data = [
        {'id': 101, 'type': 'active', 'level': 1},
        {'id': 102, 'type': 'premium', 'level': 6},
        {'id': 103, 'type': 'expired', 'level': 0},
        {'id': 104, 'type': 'default', 'level': 2},
    ]
    output = categorize_objects(data)
    print(output)