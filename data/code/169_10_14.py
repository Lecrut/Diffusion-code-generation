import threading

class ItemCounter:
    def __init__(self):
        self.item_counts = {}
        self.lock = threading.Lock()

    def increment(self, item, count=1):
        with self.lock:
            if item in self.item_counts:
                self.item_counts[item] += count
            else:
                self.item_counts[item] = count

    def decrement(self, item, count=1):
        with self.lock:
            if item in self.item_counts and self.item_counts[item] >= count:
                self.item_counts[item] -= count
                if self.item_counts[item] == 0:
                    del self.item_counts[item]

    def get_count(self, item):
        with self.lock:
            return self.item_counts.get(item, 0)

if __name__ == '__main__':
    counter = ItemCounter()
    counter.increment('apple', 3)
    counter.increment('banana')
    counter.decrement('apple', 1)
    print(f"Apple count: {counter.get_count('apple')}")
    print(f"Banana count: {counter.get_count('banana')}")