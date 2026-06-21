import threading

class ItemCounter:

    def __init__(self, initial_counts=None):
        self.counts = initial_counts if initial_counts is not None else {}
        self.lock = threading.Lock()

    def increment(self, item, amount=1):
        with self.lock:
            self.counts[item] = self.counts.get(item, 0) + amount

    def decrement(self, item, amount=1):
        with self.lock:
            if item in self.counts:
                self.counts[item] -= amount
                if self.counts[item] <= 0:
                    del self.counts[item]

    def get_count(self, item):
        with self.lock:
            return self.counts.get(item, 0)
if __name__ == '__main__':
    counter = ItemCounter({'apples': 10, 'oranges': 5})
    print(counter.get_count('apples'))
    counter.increment('apples', 3)
    print(counter.get_count('apples'))
    counter.decrement('oranges')
    print(counter.get_count('oranges'))
    counter.decrement('grapes')