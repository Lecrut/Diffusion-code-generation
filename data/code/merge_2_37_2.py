class ItemCounter:
    def __init__(self):
        self._data = {}
    def add(self, item_id, quantity):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        current_count = self._data.get(item_id, 0) + quantity
        self._data[item_id] = max(0, current_count)
    def decrement(self, item_id):
        if not isinstance(item_id, str):
            raise TypeError("Item ID must be a string.")
        current_count = self._data.get(item_id, 0) - 1
        if current_count < 0:
            return False
        elif current_count == 0:
            del self._data[item_id]
        else:
            self._data[item_id] = current_count
        return True
    def get(self, item_id):
        return self._data.get(item_id, 0)
if __name__ == '__main__':
    counter = ItemCounter()
    counter.add("apple", 5)
    counter.add("banana", 3)
    counter.decrement("apple")
    print(counter.get("apple"))
    counter.decrement("banana")
    print(counter.get("banana"))
    counter.decrement("orange")
    print(counter.get("orange"))