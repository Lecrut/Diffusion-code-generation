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
        total = 0
        for count in self._stock.values():
            total += count
        return total
if __name__ == '__main__':
    manager = InventoryManager()
    manager.increment("Apples", 50)
    manager.increment("Bananas", 100)
    manager.increment("Apples", 25)
    print(f"Stock after increments: {manager._stock}")
    print(f"Total stock: {manager.get_total_stock()}")
    manager.decrement("Apples", 10)
    manager.decrement("Oranges", 5)
    print(f"Stock after decrements: {manager._stock}")
    print(f"Total stock: {manager.get_total_stock()}")
    manager.decrement("Bananas", 150)
    print(f"Stock after large decrement: {manager._stock}")
    print(f"Total stock: {manager.get_total_stock()}")