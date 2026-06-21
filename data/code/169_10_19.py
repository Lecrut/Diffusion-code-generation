import threading

class InventoryManager:

    def __init__(self):
        self.items = {'apples': 10, 'bananas': 5}
        self.lock = threading.Lock()

    def increment(self, item, amount=1):
        with self.lock:
            if item in self.items:
                self.items[item] += amount
            else:
                raise KeyError(f'Item {item} not found')

    def decrement(self, item, amount=1):
        with self.lock:
            if item in self.items and self.items[item] >= amount:
                self.items[item] -= amount
            elif item not in self.items:
                raise KeyError(f'Item {item} not found')
            else:
                raise ValueError(f'Not enough {item} to decrement')

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