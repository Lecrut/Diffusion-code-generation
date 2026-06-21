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
                return True
            return False

    def get_inventory(self):
        with self.lock:
            return self.items.copy()

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('apple', 10)
    inventory.add_item('banana', 5)
    print(inventory.get_inventory())
    if inventory.remove_item('apple', 3):
        print(inventory.get_inventory())