import threading

class ItemCounter:

    def __init__(self):
        self.items = {'apple': 0, 'banana': 0, 'cherry': 0}
        self.lock = threading.Lock()

    def increment(self, item):
        with self.lock:
            if item in self.items:
                self.items[item] += 1

    def decrement(self, item):
        with self.lock:
            if item in self.items and self.items[item] > 0:
                self.items[item] -= 1

    def get_count(self, item):
        with self.lock:
            return self.items.get(item, 0)
if __name__ == '__main__':
    counter = ItemCounter()
    counter.increment('apple')
    counter.increment('banana')
    print(counter.get_count('apple'))
    print(counter.get_count('banana'))
    counter.decrement('apple')
    print(counter.get_count('apple'))