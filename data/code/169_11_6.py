class InventoryManager:
    def __init__(self):
        self._inventory = {}
    def increment(self, item, amount):
        if item in self._inventory:
            self._inventory[item] += amount
        else:
            self._inventory[item] = amount
    def decrement(self, item, amount):
        if item in self._inventory:
            if self._inventory[item] >= amount:
                self._inventory[item] -= amount
            else:
                self._inventory[item] = 0
        else:
            self._inventory[item] = 0
    def get_total_stock(self):
        total = sum(self._inventory.values())
        return total
if __name__ == '__main__':
    manager = InventoryManager()
    manager.increment("Apples", 50)
    manager.increment("Bananas", 100)
    manager.increment("Apples", 25)
    manager.decrement("Bananas", 30)
    manager.decrement("Oranges", 10)
    print(f"Inventory: {manager._inventory}")
    print(f"Total Stock: {manager.get_total_stock()}")