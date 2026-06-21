import threading

class Inventory:
    def __init__(self):
        self.items = []
        self.lock = threading.Lock()

    def add_item(self, item):
        with self.lock:
            self._ensure_unique(item)
            self.items.append(item)

    def remove_item(self, item):
        with self.lock:
            if item in self.items:
                self.items.remove(item)

    @staticmethod
    def _ensure_unique(item):
        if not isinstance(item, str) or len(item.strip()) == 0:
            raise ValueError("Invalid item")

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('apple')
    inventory.add_item('banana')
    print(inventory.items)
    inventory.remove_item('apple')
    print(inventory.items)