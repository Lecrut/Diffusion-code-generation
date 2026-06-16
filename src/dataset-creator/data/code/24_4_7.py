from dataclasses import dataclass
@dataclass(frozen=True)
class Item:
    name: str
    price: float
    quantity: int
def create_item_list(items_data):
    return [Item(**item_dict) for item_dict in items_data]
def calculate_total_value(item_list):
    return sum(item.price * item.quantity for item in item_list)
if __name__ == '__main__':
    sample_items = [
        {'name': 'Laptop', 'price': 1200.50, 'quantity': 3},
        {'name': 'Mouse', 'price': 25.99, 'quantity': 10},
        {'name': 'Keyboard', 'price': 75.00, 'quantity': 5}
    ]
    items = create_item_list(sample_items)
    total_value = calculate_total_value(items)
    print(f"Created {len(items)} items.")
    for item in items:
        print(f"{item.name}: ${item.price:.2f} x {item.quantity}")
    print(f"Total Value: ${total_value:.2f}")