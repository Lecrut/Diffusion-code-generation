from collections import defaultdict

class InventoryManager:
    def __init__(self):
        self.items = defaultdict(int)

    def add_batch(self, batch_items):
        for item_id, quantity in batch_items.items():
            self.items[item_id] += quantity

    def calculate_total_value(self, price_per_item):
        total_value = 0
        for item_id, quantity in self.items.items():
            total_value += quantity * price_per_item.get(item_id, 0)
        return total_value

if __name__ == '__main__':
    my_inventory = InventoryManager()
    batch_items = {
        '101': 5,
        '102': 3
    }
    my_inventory.add_batch(batch_items)
    batch_items = {
        '101': 2,
        '103': 8
    }
    my_inventory.add_batch(batch_items)
    price_per_item = {
        '101': 15.99,
        '102': 4.99,
        '103': 7.99
    }
    total_value = my_inventory.calculate_total_value(price_per_item)
    print(f"Total Inventory Value: ${total_value:.2f}")