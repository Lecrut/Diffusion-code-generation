import threading

class ItemCounter:

    def __init__(self, initial_counts=None):
        self.counts = initial_counts if initial_counts is not None else {}
        self.lock = threading.Lock()

    def increment(self, item):
        with self.lock:
            self.counts[item] = self.counts.get(item, 0) + 1

    def decrement(self, item):
        with self.lock:
            if item in self.counts:
                self.counts[item] -= 1
                if self.counts[item] == 0:
                    del self.counts[item]

    def get_count(self, item):
        with self.lock:
            return self.counts.get(item, 0)
if __name__ == '__main__':
    counter = ItemCounter({'apple': 3, 'banana': 2})
    print(counter.get_count('apple'))
    counter.increment('apple')
    print(counter.get_count('apple'))
    counter.decrement('banana')
    print(counter.get_count('banana'))
    counter.decrement('orange')
    print(counter.get_count('orange'))