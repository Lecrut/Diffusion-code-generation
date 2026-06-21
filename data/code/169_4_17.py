import threading

class ItemCounter:
    _instance = None
    _lock = threading.Lock()
    _item_counts = {}

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(ItemCounter, cls).__new__(cls)
        return cls._instance

    def update_count(self, item, amount=1):
        with self._lock:
            if item in self._item_counts:
                self._item_counts[item] += amount
            else:
                self._item_counts[item] = amount

    def get_total_unique_items(self):
        with self._lock:
            return len(self._item_counts)
if __name__ == '__main__':
    counter = ItemCounter()
    counter.update_count('apple', 3)
    counter.update_count('banana')
    print(counter.get_total_unique_items())