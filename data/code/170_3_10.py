import threading

class Inventory:

    def __init__(self):
        self.items = {}
        self.lock = threading.Lock()

    def add_item(self, item, quantity):
        with self.lock:
            if not isinstance(item, str) or not isinstance(quantity, int) or quantity < 0:
                raise ValueError('Invalid input')
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity

    def remove_item(self, item, quantity):
        with self.lock:
            if not isinstance(item, str) or not isinstance(quantity, int) or quantity < 0:
                raise ValueError('Invalid input')
            if item in self.items and self.items[item] >= quantity:
                self.items[item] -= quantity
                if self.items[item] == 0:
                    del self.items[item]
                return True
            return False
if __name__ == '__main__':
    inventory = Inventory()
    try:
        inventory.add_item('Laptop', 1)
        inventory.add_item('Mouse', 2)
        print(inventory.items)
        inventory.remove_item('Mouse', 1)
        print(inventory.items)
    except ValueError as e:
        print(e)