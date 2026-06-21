items = [
    {'id': 101, 'name': 'Milk', 'quantity': 2, 'price_per_unit': 3.99},
    {'id': 102, 'name': 'Bread', 'quantity': 1, 'price_per_unit': 2.49},
    {'id': 103, 'name': 'Eggs', 'quantity': 12, 'price_per_unit': 1.59}
]

def calculate_total_cost(items):
    total = 0
    for item in items:
        total += item['quantity'] * item['price_per_unit']
    return total

if __name__ == '__main__':
    print("Item List:")
    for item in items:
        print(f"ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}, Price per Unit: ${item['price_per_unit']:.2f}")
    
    total_cost = calculate_total_cost(items)
    print(f"\nTotal Cost: ${total_cost:.2f}")