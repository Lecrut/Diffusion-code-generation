from collections import defaultdict

class InventoryManager:
    def __init__(self):
        self.items = defaultdict(int)
    
    def add_items(self, item_dict):
        for item, quantity in item_dict.items():
            self.items[item] += quantity
    
    def calculate_total_value(self, price_dict):
        return sum(quantity * price_dict.get(item, 0) for item, quantity in self.items.items())

if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_items({'apple': 10, 'banana': 5})
    prices = {'apple': 0.5, 'banana': 0.3}
    print(manager.calculate_total_value(prices))