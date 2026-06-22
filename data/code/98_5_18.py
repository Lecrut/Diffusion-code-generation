PRIORITY_ACTIVE = 'active'
PRIORITY_PREMIUM = 'premium'
PRIORITY_EXPIRED = 'expired'
DEFAULT_STATUS = 'inactive'
STATUS_ACTIVE = 'Active'
STATUS_PREMIUM = 'Premium'
STATUS_EXPIRED = 'Expired'
STATUS_INACTIVE = 'Inactive'

def classify_items(items):
    results = []
    for item in items:
        status_code = DEFAULT_STATUS
        if item.get('status') == PRIORITY_ACTIVE:
            status_code = STATUS_ACTIVE
        elif item.get('type') == PRIORITY_PREMIUM:
            status_code = STATUS_PREMIUM
        elif item.get('expiry_date') is not None and item.get('expiry_date') < '2023-01-01':
            status_code = STATUS_EXPIRED
        
        results.append({
            'id': item.get('id'),
            'name': item.get('name'),
            'final_status': status_code
        })
    return results

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alpha', 'status': 'active', 'type': 'standard', 'expiry_date': '2024-05-01'},
        {'id': 2, 'name': 'Beta', 'status': 'inactive', 'type': 'premium', 'expiry_date': '2025-01-01'},
        {'id': 3, 'name': 'Gamma', 'status': 'inactive', 'type': 'standard', 'expiry_date': '2022-12-31'},
        {'id': 4, 'name': 'Delta', 'status': 'inactive', 'type': 'standard', 'expiry_date': None}
    ]
    output = classify_items(sample_data)
    print(output)