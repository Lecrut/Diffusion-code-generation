import threading

class ItemCounter:
    _instance = None
    _lock = threading.Lock()
    _counts = {}

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(ItemCounter, cls).__new__(cls)
        return cls._instance

    def update_count(self, item, amount=1):
        if not isinstance(item, str) or not isinstance(amount, int) or amount < 0:
            raise ValueError('Invalid input: item must be a string and amount must be a non-negative integer')
        with self._lock:
            if item in self._counts:
                self._counts[item] += amount
            else:
                self._counts[item] = amount

    def get_total_unique_items(self):
        with self._lock:
            return len(self._counts)
if __name__ == '__main__':
    counter = ItemCounter()
    counter.update_count('apple', 5)
    counter.update_count('banana', 3)
    print(counter.get_total_unique_items())