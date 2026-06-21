def optimize_inventory(items):
    return sum(item['quantity'] for item in items)

if __name__ == '__main__':
    sample_items = [
        {'item': 'apple', 'quantity': 30},
        {'item': 'banana', 'quantity': 45},
        {'item': 'orange', 'quantity': 20}
    ]
    print(optimize_inventory(sample_items))