import threading

class Inventory:
    def __init__(self):
        self.items = []
        self.lock = threading.Lock()

    def add_item(self, item):
        with self.lock:
            if item not in self.items:
                self.items.append(item)

    def remove_item(self, item):
        with self.lock:
            if item in self.items:
                self.items.remove(item)

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('apple')
    inventory.add_item('banana')
    print("Added items:", inventory.items)
    inventory.remove_item('apple')
    print("Removed apple, remaining items:", inventory.items)