import threading

class InventoryManager:

    def __init__(self):
        self.items = {'apples': 10, 'bananas': 5}
        self.lock = threading.Lock()

    def increment(self, item, count=1):
        with self.lock:
            if item in self.items:
                self.items[item] += count
            else:
                raise ValueError(f'Item {item} not found')

    def decrement(self, item, count=1):
        with self.lock:
            if item in self.items and self.items[item] >= count:
                self.items[item] -= count
            elif item not in self.items:
                raise ValueError(f'Item {item} not found')
            else:
                raise ValueError(f'Not enough {item}s to decrement')

    def get_count(self, item):
        with self.lock:
            return self.items.get(item, 0)
if __name__ == '__main__':
    manager = InventoryManager()
    print(manager.get_count('apples'))
    manager.increment('apples', 5)
    print(manager.get_count('apples'))
    manager.decrement('bananas')
    print(manager.get_count('bananas'))