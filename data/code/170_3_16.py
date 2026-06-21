import threading

class Inventory:
    def __init__(self):
        self.items = {}
        self.lock = threading.Lock()

    def add_item(self, item, quantity):
        if not isinstance(item, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid input: item must be a string and quantity must be a non-negative integer")
        with self.lock:
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity

    def remove_item(self, item, quantity):
        if not isinstance(item, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid input: item must be a string and quantity must be a non-negative integer")
        with self.lock:
            if item in self.items and self.items[item] >= quantity:
                self.items[item] -= quantity
                if self.items[item] == 0:
                    del self.items[item]
                return True
            else:
                return False

    def get_inventory(self):
        with self.lock:
            return self.items.copy()

if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Laptop", 1)
    my_inventory.add_item("Mouse", 2)
    my_inventory.add_item("Keyboard", 3)
    print(my_inventory.get_inventory())
    my_inventory.remove_item("Mouse", 1)
    print(my_inventory.get_inventory())