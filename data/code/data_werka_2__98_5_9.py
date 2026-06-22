def process_items(items):
    results = []
    for item in items:
        name = item.get('name', '')
        status = item.get('status', '')
        is_premium = item.get('is_premium', False)
        
        if status == 'active' and is_premium:
            results.append({'name': name, 'category': 'premium_active', 'score': 100})
        elif status == 'active' and not is_premium:
            results.append({'name': name, 'category': 'standard_active', 'score': 50})
        elif status == 'expired' and is_premium:
            results.append({'name': name, 'category': 'premium_expired', 'score': 10})
        elif status == 'expired' and not is_premium:
            results.append({'name': name, 'category': 'standard_expired', 'score': 0})
        else:
            results.append({'name': name, 'category': 'unknown', 'score': 0})
            
    return results

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'status': 'active', 'is_premium': True},
        {'name': 'Bob', 'status': 'active', 'is_premium': False},
        {'name': 'Charlie', 'status': 'expired', 'is_premium': True},
        {'name': 'Diana', 'status': 'expired', 'is_premium': False},
        {'name': 'Eve', 'status': 'inactive', 'is_premium': True}
    ]
    
    processed = process_items(sample_data)
    print(processed)