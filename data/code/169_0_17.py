class ItemCounter:

    def __init__(self, initial_counts=None):
        self.counts = initial_counts if initial_counts is not None else {}

    def increment(self, item_name, quantity=1):
        with self._lock():
            self.counts[item_name] = self.counts.get(item_name, 0) + quantity

    def decrement(self, item_name, quantity=1):
        with self._lock():
            if item_name in self.counts:
                new_count = self.counts[item_name] - quantity
                if new_count > 0:
                    self.counts[item_name] = new_count
                else:
                    del self.counts[item_name]

    def get_count(self, item_name):
        with self._lock():
            return self.counts.get(item_name, 0)

    @staticmethod
    def _lock():
        import threading
        lock = threading.Lock()
        return lock
if __name__ == '__main__':
    counter = ItemCounter({'apples': 10, 'oranges': 5})
    print(counter.get_count('apples'))
    counter.increment('apples', 3)
    print(counter.get_count('apples'))
    counter.decrement('oranges')
    print(counter.get_count('oranges'))
    counter.decrement('grapes', 2)
    print(counter.get_count('grapes'))