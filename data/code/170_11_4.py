class InventoryManager:

    def __init__(self, initial_items):
        self.stock = {item: 0 for item in initial_items}

    def update_stock(self, item, quantity):
        if item in self.stock:
            self.stock[item] += quantity

    def check_availability(self, item, quantity):
        return self.stock.get(item, 0) >= quantity
if __name__ == '__main__':
    manager = InventoryManager(['apple', 'banana'])
    manager.update_stock('apple', 10)
    print(manager.check_availability('apple', 5))
    print(manager.check_availability('banana', 3))