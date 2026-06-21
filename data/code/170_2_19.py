from collections import defaultdict

class InventoryManager:
    def __init__(self, item_price):
        self.inventory = defaultdict(int)
        self.item_price = item_price

    def add_items(self, items):
        for item, quantity in items.items():
            self.inventory[item] += quantity

    def calculate_total_value(self):
        return sum(quantity * self.item_price[item] for item, quantity in self.inventory.items())

if __name__ == '__main__':
    manager = InventoryManager({'apple': 0.5, 'banana': 0.3})
    manager.add_items({'apple': 10, 'banana': 20})
    print(manager.calculate_total_value())