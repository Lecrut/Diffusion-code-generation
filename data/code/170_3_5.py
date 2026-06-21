import threading

class Inventory:
    def __init__(self):
        self.items = {}
        self.lock = threading.Lock()

    def add_item(self, item, quantity):
        with self.lock:
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity

    def remove_item(self, item, quantity):
        with self.lock:
            if item in self.items and self.items[item] >= quantity:
                self.items[item] -= quantity
                if self.items[item] == 0:
                    del self.items[item]
            else:
                raise ValueError("Not enough inventory")

    def get_inventory(self):
        with self.lock:
            return self.items.copy()

if __name__ == '__main__':
    inv = Inventory()
    inv.add_item('apple', 10)
    inv.add_item('banana', 5)
    print(inv.get_inventory())
    inv.remove_item('apple', 3)
    print(inv.get_inventory())