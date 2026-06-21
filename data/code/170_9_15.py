CONVERSION_FACTOR = 1.2

def calculate_total(items):
    return sum(item['quantity'] * item['price'] * CONVERSION_FACTOR for item in items)

def filter_items_by_threshold(items, threshold):
    return list(filter(lambda x: x['quantity'] > threshold, items))

if __name__ == '__main__':
    sample_items = [
        {'item_id': 1, 'name': 'apple', 'quantity': 30, 'price': 0.5},
        {'item_id': 2, 'name': 'banana', 'quantity': 40, 'price': 0.3}
    ]
    
    total_value = calculate_total(sample_items)
    print(f"Total inventory value: {total_value:.2f}")
    
    filtered_items = filter_items_by_threshold(sample_items, 25)
    print("--- Items above threshold ---")
    for item in filtered_items:
        print(item['name'], item['quantity'])