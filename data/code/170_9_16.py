def calculate_inventory_value(items):
    return sum(item['quantity'] * item['price'] for item in items)

if __name__ == '__main__':
    sample_items = [
        {'item_id': '001', 'name': 'Laptop', 'quantity': 5, 'price': 999},
        {'item_id': '002', 'name': 'Mouse', 'quantity': 20, 'price': 25},
        {'item_id': '003', 'name': 'Keyboard', 'quantity': 15, 'price': 75}
    ]
    inventory_value = calculate_inventory_value(sample_items)
    print(f"Total Inventory Value: ${inventory_value}")