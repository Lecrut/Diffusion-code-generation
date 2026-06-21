CONVERSION_FACTOR = 1.0

def calculate_inventory_cost(items):
    return sum((item['quantity'] * item['price'] for item in items))

def update_item_quantity(items, item_id, quantity_change):
    if item_id in items:
        items[item_id]['quantity'] += quantity_change
    else:
        raise ValueError('Item ID not found')
if __name__ == '__main__':
    sample_items = [{'id': 1, 'name': 'Widget', 'quantity': 50, 'price': 2.99}, {'id': 2, 'name': 'Gadget', 'quantity': 30, 'price': 4.99}]
    print('Initial Inventory Cost:', calculate_inventory_cost(sample_items))
    update_item_quantity(sample_items, 1, 10)
    print('Updated Inventory Cost:', calculate_inventory_cost(sample_items))