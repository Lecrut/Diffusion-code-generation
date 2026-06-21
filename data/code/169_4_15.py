import threading

class ItemCounter:
    _instance = None
    _lock = threading.Lock()
    _counts = {}

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ItemCounter, cls).__new__(cls)
        return cls._instance

    def update_count(self, item, amount=1):
        with self._lock:
            if item not in self._counts:
                self._counts[item] = 0
            self._counts[item] += amount

    def get_total_unique_items(self):
        with self._lock:
            return len(self._counts)
if __name__ == '__main__':
    ic = ItemCounter()
    ic.update_count('apple', 3)
    ic.update_count('banana')
    ic.update_count('apple', 2)
    print(ic.get_total_unique_items())