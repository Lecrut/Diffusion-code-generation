def optimized_inventory_calculator(items):
    return sum(item['quantity'] for item in items)

if __name__ == '__main__':
    sample_items = [
        {'item': 'apple', 'quantity': 10},
        {'item': 'banana', 'quantity': 20},
        {'item': 'orange', 'quantity': 30}
    ]
    print(optimized_inventory_calculator(sample_items))