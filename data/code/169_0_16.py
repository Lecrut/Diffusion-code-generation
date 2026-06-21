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
    counter = ItemCounter({'apples': 3, 'oranges': 2})
    print(counter.get_count('apples'))
    counter.increment('apples', 2)
    print(counter.get_count('apples'))
    counter.decrement('oranges')
    print(counter.get_count('oranges'))
    counter.decrement('grapes')
    print(counter.get_count('grapes'))