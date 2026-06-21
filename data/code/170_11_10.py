class InventoryManager:

    def __init__(self, initial_items):
        self.stock = {item: 0 for item in initial_items}

    def update_stock(self, item, amount):
        if item in self.stock:
            self.stock[item] += amount

    def check_availability(self, item):
        return self.stock.get(item, 0) > 0
if __name__ == '__main__':
    manager = InventoryManager(['apple', 'banana', 'cherry'])
    manager.update_stock('apple', 10)
    print(manager.check_availability('apple'))
    manager.update_stock('banana', -5)
    print(manager.check_availability('banana'))