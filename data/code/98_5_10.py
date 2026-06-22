def classify_items(items):
    if not isinstance(items, list):
        raise ValueError("Items must be a list")
    
    VALID_STATUSES = {'active', 'premium', 'expired', 'inactive'}
    processed_items = []
    
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("Each item must be a dictionary")
        
        current_status = item.get('status', 'inactive')
        is_premium = item.get('premium', False)
        expiry_date = item.get('expiry_date')
        
        final_status = current_status
        
        if is_premium:
            final_status = 'premium'
        elif expiry_date:
            if expiry_date < '2023-01-01':
                final_status = 'expired'
            elif expiry_date > '2025-12-31':
                final_status = 'inactive'
        
        if final_status not in VALID_STATUSES:
            raise ValueError(f"Invalid computed status: {final_status}")
        
        processed_items.append({
            'original_id': item.get('id'),
            'final_status': final_status,
            'is_premium_flag': is_premium
        })
    
    return processed_items

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'User Alpha', 'status': 'active', 'premium': False, 'expiry_date': '2024-06-15'},
        {'id': 2, 'name': 'User Beta', 'status': 'inactive', 'premium': True, 'expiry_date': None},
        {'id': 3, 'name': 'User Gamma', 'status': 'active', 'premium': False, 'expiry_date': '2022-11-20'},
        {'id': 4, 'name': 'User Delta', 'status': 'inactive', 'premium': False, 'expiry_date': '2026-01-01'},
    ]
    
    result = classify_items(sample_data)
    print(result)