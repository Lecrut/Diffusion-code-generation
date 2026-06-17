class Inventory:
    def __init__(self):
        self._data = {}
    def add(self, item, quantity):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        current_qty = self._data.get(item, 0) + quantity
        self._data[item] = max(0, current_qty)
    def decrement(self, item):
        if not isinstance(item, str):
            raise TypeError("Item name must be a string.")
        current_qty = self._data.get(item, 0) - 1
        if current_qty < 0:
            return False
        elif current_qty == 0:
            del self._data[item]
        else:
            self._data[item] = current_qty
        return True
    def get(self, item):
        return self._data.get(item, 0)
    def __repr__(self):
        return f"Inventory({dict(sorted(self._data.items()))})"
if __name__ == '__main__':
    inv = Inventory()
    inv.add("apple", 5)
    inv.add("banana", 3)
    inv.decrement("apple")
    print(inv.get("apple"))
    inv.decrement("banana")
    print(inv.get("banana"))
    inv.decrement("orange")