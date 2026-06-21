def process_items(items):
    results = []
    for item in items:
        name = item.get('name', '')
        status = item.get('status', '')
        is_premium = item.get('premium', False)
        
        if status == 'active' and is_premium:
            results.append({'name': name, 'category': 'premium_active', 'score': 100})
        elif status == 'active':
            results.append({'name': name, 'category': 'standard_active', 'score': 50})
        elif status == 'expired' and is_premium:
            results.append({'name': name, 'category': 'premium_expired', 'score': 10})
        elif status == 'expired':
            results.append({'name': name, 'category': 'standard_expired', 'score': 0})
        else:
            results.append({'name': name, 'category': 'unknown', 'score': 0})
            
    return results

if __name__ == '__main__':
    sample_data = [
        {'name': 'User1', 'status': 'active', 'premium': True},
        {'name': 'User2', 'status': 'active', 'premium': False},
        {'name': 'User3', 'status': 'expired', 'premium': True},
        {'name': 'User4', 'status': 'expired', 'premium': False},
        {'name': 'User5', 'status': 'inactive', 'premium': False}
    ]
    
    output = process_items(sample_data)
    print(output)