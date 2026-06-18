from dataclasses import dataclass
@dataclass(frozen=True)
class Item:
    id: int
    name: str
    price: float
    quantity: int
def create_item_list(items_data):
    return [Item(**item_dict) for item_dict in items_data]
def calculate_total_price(item_list):
    total = sum(item.price * item.quantity for item in item_list)
    return round(total, 2)
if __name__ == '__main__':
    sample_items = [
        {"id": 101, "name": "Laptop", "price": 999.99, "quantity": 5},
        {"id": 102, "name": "Mouse", "price": 25.50, "quantity": 20},
        {"id": 103, "name": "Keyboard", "price": 75.00, "quantity": 10}
    ]
    item_list = create_item_list(sample_items)
    total_cost = calculate_total_price(item_list)
    print(f"Total Cost: {total_cost}")