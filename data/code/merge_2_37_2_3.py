class ItemCounter:
    def __init__(self):
        self._data = {}
    def add(self, key: str, quantity: int) -> None:
        if not isinstance(quantity, (int, float)):
            raise TypeError("Quantity must be a number")
        current_value = self._data.get(key, 0)
        new_value = current_value + quantity
        if new_value > 0:
            self._data[key] = new_value
    def decrement(self, key: str) -> bool:
        try:
            current_value = self._data.get(key, 0)
            if not isinstance(current_value, (int, float)):
                return False
            if current_value <= 1:
                del self._data[key]
                return True
            new_value = int(current_value - 1)
            self._data[key] = new_value
            return True
        except Exception:
            return False
    def get(self, key: str) -> int | None:
        value = self._data.get(key)
        if value is not None and isinstance(value, (int, float)):
            return int(value)
        return 0
    def __contains__(self, key):
        return key in self._data
if __name__ == '__main__':
    counter = ItemCounter()
    counter.add("apple", 5)
    counter.add("banana", 3)
    counter.decrement("apple")
    counter.decrement("apple")
    counter.decrement("apple")
    counter.decrement("banana")
    counter.decrement("orange")                                      
    print(f"Apple count: {counter.get('apple')}")
    print(f"Banana count: {counter.get('banana')}")
    print(f"Orange exists: {'orange' in counter}")