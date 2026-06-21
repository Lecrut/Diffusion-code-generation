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

    def add_item(self, item):
        with self._lock:
            if item in self._counts:
                self._counts[item] += 1
            else:
                self._counts[item] = 1

    def get_total_items(self):
        with self._lock:
            return len(self._counts)
if __name__ == '__main__':
    counter = ItemCounter()
    counter.add_item('apple')
    counter.add_item('banana')
    counter.add_item('apple')
    print(counter.get_total_items())