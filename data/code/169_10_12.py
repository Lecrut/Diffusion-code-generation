import threading

class ItemCounter:

    def __init__(self):
        self.items = {'apple': 5, 'banana': 3}
        self.lock = threading.Lock()

    def increment(self, item):
        with self.lock:
            if item in self.items:
                self.items[item] += 1
            else:
                raise KeyError(f"Item '{item}' not found")

    def decrement(self, item):
        with self.lock:
            if item in self.items:
                if self.items[item] > 0:
                    self.items[item] -= 1
                else:
                    raise ValueError(f"Cannot decrement item '{item}' as it is already zero")
            else:
                raise KeyError(f"Item '{item}' not found")

    def get_count(self, item):
        with self.lock:
            if item in self.items:
                return self.items[item]
            else:
                raise KeyError(f"Item '{item}' not found")
if __name__ == '__main__':
    counter = ItemCounter()
    print(counter.get_count('apple'))
    counter.increment('apple')
    print(counter.get_count('apple'))
    counter.decrement('banana')
    print(counter.get_count('banana'))