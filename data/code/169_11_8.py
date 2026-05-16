class InventoryManager:
    def __init__(self):
        self._stock = {}
    def increment(self, item, amount):
        if item in self._stock:
            self._stock[item] += amount
        else:
            self._stock[item] = amount
    def decrement(self, item, amount):
        if item in self._stock:
            if self._stock[item] >= amount:
                self._stock[item] -= amount
            else:
                self._stock[item] = 0
        else:
            self._stock[item] = 0
    def get_total_stock(self):
        total = sum(self._stock.values())
        return total
if __name__ == '__main__':
    manager = InventoryManager()
    manager.increment("Apples", 100)
    manager.increment("Bananas", 50)
    manager.increment("Apples", 25)
    print(f"Apples stock: {manager._stock.get('Apples', 0)}")
    print(f"Bananas stock: {manager._stock.get('Bananas', 0)}")
    print(f"Total stock: {manager.get_total_stock()}")
    manager.decrement("Apples", 30)
    manager.decrement("Oranges", 10)
    print(f"Apples stock after decrement: {manager._stock.get('Apples', 0)}")
    print(f"Bananas stock after decrement: {manager._stock.get('Bananas', 0)}")
    print(f"Oranges stock after decrement: {manager._stock.get('Oranges', 0)}")
    print(f"Total stock after decrement: {manager.get_total_stock()}")