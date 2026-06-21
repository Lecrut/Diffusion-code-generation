def calculate_inventory_value(items):
    return sum(item['quantity'] * item['price'] for item in items)

if __name__ == '__main__':
    sample_items = [
        {'item_id': '101', 'name': 'Widget A', 'quantity': 5, 'price': 2.99},
        {'item_id': '102', 'name': 'Gadget B', 'quantity': 3, 'price': 4.50},
        {'item_id': '103', 'name': 'Doodad C', 'quantity': 10, 'price': 1.99}
    ]
    total_value = calculate_inventory_value(sample_items)
    print(f"Total Inventory Value: ${total_value:.2f}")