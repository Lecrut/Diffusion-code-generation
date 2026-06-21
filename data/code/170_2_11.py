from collections import defaultdict

class InventoryManager:
    def __init__(self):
        self.items = defaultdict(int)

    def add_item(self, item_id, quantity):
        self.items[item_id] += quantity

    def calculate_total_value(self, price_per_item):
        total_value = 0
        for item_id, quantity in self.items.items():
            total_value += quantity * price_per_item.get(item_id, 0)
        return total_value

if __name__ == '__main__':
    inventory_manager = InventoryManager()
    inventory_manager.add_item(101, 50)
    inventory_manager.add_item(102, 30)
    inventory_manager.add_item(101, 10)

    prices = {101: 0.5, 102: 0.3}
    total_value = inventory_manager.calculate_total_value(prices)
    print(f"Total Inventory Value: ${total_value:.2f}")