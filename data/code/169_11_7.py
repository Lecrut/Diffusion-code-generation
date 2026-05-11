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
        total = 0
        for count in self._inventory.values():
            total += count
        return total
if __name__ == '__main__':
    manager = InventoryManager()
    manager.increment("Apples", 100)
    manager.increment("Bananas", 50)
    manager.increment("Apples", 20)
    print(f"Apples stock: {manager._inventory.get('Apples', 0)}")
    print(f"Bananas stock: {manager._inventory.get('Bananas', 0)}")
    print(f"Total stock: {manager.get_total_stock()}")
    manager.decrement("Apples", 30)
    manager.decrement("Oranges", 10)
    print(f"Apples stock after decrement: {manager._inventory.get('Apples', 0)}")
    print(f"Bananas stock after decrement: {manager._inventory.get('Bananas', 0)}")
    print(f"Oranges stock after decrement: {manager._inventory.get('Oranges', 0)}")
    print(f"Total stock after decrement: {manager.get_total_stock()}")