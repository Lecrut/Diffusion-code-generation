import threading

class Inventory:

    def __init__(self):
        self.items = []
        self.lock = threading.Lock()

    def _validate_item(self, item):
        if not isinstance(item, str) or not item.strip():
            raise ValueError('Item must be a non-empty string')

    def add_item(self, item):
        with self.lock:
            self._validate_item(item)
            if item not in self.items:
                self.items.append(item)

    def remove_item(self, item):
        with self.lock:
            self._validate_item(item)
            if item in self.items:
                self.items.remove(item)
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('apple')
    inventory.add_item('banana')
    print(inventory.items)
    inventory.remove_item('apple')
    print(inventory.items)