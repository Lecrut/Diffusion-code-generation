from collections import defaultdict

class InventoryManager:
    def __init__(self):
        self.items = defaultdict(int)

    def add_items(self, items):
        for item, quantity in items.items():
            self.items[item] += quantity

    def calculate_total_value(self, price_per_item):
        return sum(quantity * price_per_item.get(item, 0) for item, quantity in self.items.items())

if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_items({'apple': 10, 'banana': 5})
    print(manager.calculate_total_value({'apple': 2.0, 'banana': 1.5}))