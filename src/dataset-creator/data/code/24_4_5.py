from dataclasses import dataclass
@dataclass(frozen=True)
class Item:
    id: int
    name: str
    price: float
    quantity: int
def create_item_list(items_data):
    return [Item(**item_dict) for item_dict in items_data]
def calculate_total_value(item_list):
    total = sum(item.price * item.quantity for item in item_list)
    return round(total, 2)
def filter_by_price_range(item_list, min_price: float, max_price: float):
    filtered_items = [item for item in item_list if min_price <= item.price <= max_price]
    return filtered_items
if __name__ == '__main__':
    sample_data = [
        {'id': 101, 'name': 'Laptop', 'price': 999.50, 'quantity': 2},
        {'id': 102, 'name': 'Mouse', 'price': 25.00, 'quantity': 5},
        {'id': 103, 'name': 'Keyboard', 'price': 75.99, 'quantity': 3}
    ]
    items = create_item_list(sample_data)
    total_value = calculate_total_value(items)
    filtered_items = filter_by_price_range(items, 20.0, 100.0)
    print(f"Total Value: {total_value}")