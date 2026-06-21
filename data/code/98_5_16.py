def process_items(items):
    results = []
    for item in items:
        status = item.get('status', '')
        is_premium = item.get('is_premium', False)
        price = item.get('price', 0)
        
        if status == 'active' and is_premium:
            final_price = price * 0.8
            results.append({'id': item['id'], 'final_price': final_price, 'note': 'Premium Active Discount'})
        elif status == 'active':
            final_price = price
            results.append({'id': item['id'], 'final_price': final_price, 'note': 'Standard Active'})
        elif status == 'expired':
            final_price = 0
            results.append({'id': item['id'], 'final_price': final_price, 'note': 'Expired Item'})
        else:
            final_price = price * 0.5
            results.append({'id': item['id'], 'final_price': final_price, 'note': 'Other Status Discount'})
            
    return results

if __name__ == '__main__':
    sample_items = [
        {'id': 1, 'status': 'active', 'is_premium': True, 'price': 100},
        {'id': 2, 'status': 'active', 'is_premium': False, 'price': 50},
        {'id': 3, 'status': 'expired', 'is_premium': True, 'price': 200},
        {'id': 4, 'status': 'inactive', 'is_premium': False, 'price': 75}
    ]
    
    processed = process_items(sample_items)
    print(processed)