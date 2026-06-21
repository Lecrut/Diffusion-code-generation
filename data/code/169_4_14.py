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
            current_count = self._item_counts.get(item, 0)
            self._item_counts[item] = current_count + amount

    def get_total_unique_items(self):
        with self._lock:
            return len(self._item_counts)
if __name__ == '__main__':
    counter = ItemCounter()
    counter.update_count('apple', 3)
    counter.update_count('banana', 1)
    counter.update_count('apple', 2)
    print(counter.get_total_unique_items())