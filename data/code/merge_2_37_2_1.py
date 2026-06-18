class Counter:
    def __init__(self):
        self._items = {}
    def increment(self, item, amount=1):
        if item not in self._items or self._items[item] <= 0:
            self._items[item] = amount
        else:
            self._items[item] += amount
    def decrement(self, item, amount=1):
        current_value = self._items.get(item, 0) - amount
        if current_value > 0:
            self._items[item] = current_value
    def get_quantity(self, item):
        return self._items.get(item, 0)
    def list_items(self):
        return [item for item in sorted(self._items.keys())]
if __name__ == '__main__':
    counter = Counter()
    counter.increment('apple', 5)
    counter.increment('banana', 3)
    counter.decrement('apple', 2)
    print("Quantities:", {item: quantity for item, quantity in sorted(counter._items.items())})