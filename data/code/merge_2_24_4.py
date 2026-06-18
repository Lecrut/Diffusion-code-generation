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
def filter_by_price_range(item_list, min_price: float | None = None, max_price: float | None = None):
    filtered_items = []
    for item in item_list:
        if (min_price is not None and item.price < min_price) or\
           (max_price is not None and item.price > max_price):
            continue
        filtered_items.append(item)
    return filtered_items
def update_quantity(item_list, target_id: int, new_quantity: int):
    updated_item = next((item for item in item_list if item.id == target_id), None)
    if not updated_item:
        raise ValueError(f"Item with id {target_id} not found.")
    return [item if item.id != target_id else Item(id=item.id, name=item.name, price=item.price, quantity=new_quantity) for item in item_list]
if __name__ == '__main__':
    sample_data = [
        {"id": 101, "name": "Laptop", "price": 999.50, "quantity": 2},
        {"id": 102, "name": "Mouse", "price": 25.00, "quantity": 5},
        {"id": 103, "name": "Keyboard", "price": 75.99, "quantity": 3}
    ]
    items = create_item_list(sample_data)
    total_value = calculate_total_value(items)
    print(f"Total Value: {total_value}")
    filtered_items = filter_by_price_range(items, min_price=100.0)
    for item in filtered_items:
        print(item.name + f": ${item.price:.2f} x {item.quantity}")
    updated_list = update_quantity(items, 101, 5)
    total_value_after_update = calculate_total_value(updated_list)
    print(f"Total Value After Update: {total_value_after_update}")