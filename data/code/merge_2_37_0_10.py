import threading
from collections import defaultdict
class ThreadSafeCounter:
    def __init__(self):
        self._data = defaultdict(int)
        self._lock = threading.Lock()
    def increment(self, item):
        with self._lock:
            self._data[item] += 1
    def decrement(self, item):
        with self._lock:
            if self._data[item] > 0:
                self._data[item] -= 1
    def get_count(self, item):
        with self._lock:
            return self._data.get(item, 0)
if __name__ == '__main__':
    counter = ThreadSafeCounter()
    for _ in range(5):
        counter.increment("apple")
    for _ in range(3):
        counter.decrement("banana")
    print(f"Apple count: {counter.get_count('apple')}")
    print(f"Banana count: {counter.get_count('banana')}")