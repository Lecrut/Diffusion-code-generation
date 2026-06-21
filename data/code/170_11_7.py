class Inventory:

    def __init__(self, items):
        self.stock = {item: 0 for item in items}

    def update_stock(self, item, quantity):
        if item in self.stock:
            self.stock[item] += quantity

    def check_availability(self, item):
        return self.stock.get(item, 0) > 0
if __name__ == '__main__':
    inventory = Inventory(['apple', 'banana', 'orange'])
    inventory.update_stock('apple', 10)
    inventory.update_stock('banana', 5)
    print(inventory.check_availability('apple'))
    print(inventory.check_availability('banana'))
    print(inventory.check_availability('cherry'))