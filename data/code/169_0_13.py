import threading

class ItemCounter:

    def __init__(self, initial_counts=None):
        self.lock = threading.Lock()
        if initial_counts is None:
            initial_counts = {}
        self.counts = {item: max(count, 0) for item, count in initial_counts.items()}

    def increment(self, item_name, quantity=1):
        with self.lock:
            self.counts[item_name] = max(0, self.counts.get(item_name, 0) + quantity)

    def decrement(self, item_name, quantity=1):
        with self.lock:
            if item_name in self.counts:
                self.counts[item_name] = max(0, self.counts[item_name] - quantity)
            else:
                raise KeyError(f"Item '{item_name}' not found.")

    def get_count(self, item_name):
        with self.lock:
            return self.counts.get(item_name, 0)
if __name__ == '__main__':
    counter = ItemCounter({'apples': 10, 'bananas': 5})
    print(counter.get_count('apples'))
    counter.increment('apples', 3)
    print(counter.get_count('apples'))
    counter.decrement('bananas', 2)
    print(counter.get_count('bananas'))
    try:
        counter.decrement('oranges')
    except KeyError as e:
        print(e)