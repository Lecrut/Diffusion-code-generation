import threading

class Inventory:

    def __init__(self):
        self.items = {'apples': 0, 'bananas': 0, 'oranges': 0}
        self.lock = threading.Lock()

    def increment(self, item, count=1):
        with self.lock:
            if item in self.items:
                self.items[item] += count

    def decrement(self, item, count=1):
        with self.lock:
            if item in self.items and self.items[item] >= count:
                self.items[item] -= count

    def get_count(self, item):
        with self.lock:
            return self.items.get(item, 0)
if __name__ == '__main__':
    inventory = Inventory()
    inventory.increment('apples', 5)
    inventory.increment('bananas', 3)
    print(inventory.get_count('apples'))
    print(inventory.get_count('bananas'))
    inventory.decrement('apples', 2)
    print(inventory.get_count('apples'))