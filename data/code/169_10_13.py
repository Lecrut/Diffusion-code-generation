import threading

class Inventory:

    def __init__(self):
        self.items = {'apples': 10, 'bananas': 5}
        self.lock = threading.Lock()

    def increment(self, item):
        with self.lock:
            if item in self.items:
                self.items[item] += 1
                return self.items[item]
            else:
                raise KeyError(f"Item '{item}' not found")

    def decrement(self, item):
        with self.lock:
            if item in self.items and self.items[item] > 0:
                self.items[item] -= 1
                return self.items[item]
            elif item not in self.items:
                raise KeyError(f"Item '{item}' not found")
            else:
                raise ValueError(f'Not enough {item} to decrement')

    def get_count(self, item):
        with self.lock:
            if item in self.items:
                return self.items[item]
            else:
                raise KeyError(f"Item '{item}' not found")
if __name__ == '__main__':
    inventory = Inventory()
    print(inventory.increment('apples'))
    print(inventory.decrement('bananas'))
    print(inventory.get_count('apples'))