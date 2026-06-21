import threading

class ItemCounter:

    def __init__(self, initial_counts=None):
        self.counts = initial_counts if initial_counts is not None else {}
        self.lock = threading.Lock()

    def increment(self, item, amount=1):
        with self.lock:
            if item in self.counts:
                self.counts[item] += amount
            else:
                self.counts[item] = amount

    def decrement(self, item, amount=1):
        with self.lock:
            if item in self.counts:
                self.counts[item] -= amount
                if self.counts[item] < 0:
                    self.counts[item] = 0

    def get_count(self, item):
        with self.lock:
            return self.counts.get(item, 0)
if __name__ == '__main__':
    counter = ItemCounter({'apple': 3, 'banana': 2})
    print(counter.get_count('apple'))
    counter.increment('apple')
    print(counter.get_count('apple'))
    counter.decrement('banana', 3)
    print(counter.get_count('banana'))