from collections import defaultdict

class InventoryManager:
    def __init__(self):
        self.items = defaultdict(int)

    def add_items(self, items):
        for item, quantity in items.items():
            self.items[item] += quantity

    def calculate_total_value(self, prices):
        total_value = 0
        for item, price in prices.items():
            total_value += self.items[item] * price
        return total_value

if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_items({'apple': 10, 'banana': 5})
    prices = {'apple': 0.50, 'banana': 0.30}
    print(manager.calculate_total_value(prices))