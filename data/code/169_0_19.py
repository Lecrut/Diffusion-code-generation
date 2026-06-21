import threading

class ItemCounter:

    def __init__(self, initial_counts=None):
        if initial_counts is None:
            initial_counts = {}
        self._counts = initial_counts.copy()
        self._lock = threading.Lock()

    def increment(self, item):
        with self._lock:
            self._counts[item] = self._counts.get(item, 0) + 1

    def decrement(self, item):
        with self._lock:
            if item in self._counts:
                self._counts[item] -= 1
                if self._counts[item] == 0:
                    del self._counts[item]

    def get_count(self, item):
        with self._lock:
            return self._counts.get(item, 0)
if __name__ == '__main__':
    counter = ItemCounter({'apple': 3, 'banana': 2})
    print(counter.get_count('apple'))
    counter.increment('apple')
    print(counter.get_count('apple'))
    counter.decrement('banana')
    print(counter.get_count('banana'))
    counter.decrement('orange')
    print(counter.get_count('orange'))