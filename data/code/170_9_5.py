def calculate_inventory(item_data):
    return sum(item['quantity'] for item in item_data)

if __name__ == '__main__':
    sample_items = [
        {'item': 'apple', 'quantity': 10},
        {'item': 'banana', 'quantity': 20},
        {'item': 'orange', 'quantity': 30}
    ]
    print(calculate_inventory(sample_items))