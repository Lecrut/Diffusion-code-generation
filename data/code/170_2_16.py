from collections import defaultdict

class InventoryManager:
    def __init__(self):
        self.items = defaultdict(int)

    def add_items(self, items):
        for item_id, quantity in items.items():
            if quantity < 0:
                raise ValueError(f"Quantity {quantity} cannot be negative.")
            self.items[item_id] += quantity

    def get_total_value(self, price_per_item):
        return sum(item_id * price_per_item[item_id] for item_id in self.items)

if __name__ == '__main__':
    my_inventory = InventoryManager()
    items_to_add = {101: 50, 102: 30}
    try:
        my_inventory.add_items(items_to_add)
        print(f"Inventory updated successfully.")
    except ValueError as e:
        print(f"Error: {e}")

    price_per_item = {101: 1.0, 102: 0.5}
    total_value = my_inventory.get_total_value(price_per_item)
    print(f"Total inventory value: ${total_value:.2f}")