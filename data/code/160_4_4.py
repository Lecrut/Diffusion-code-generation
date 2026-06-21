from threading import Lock

class Inventory:
    def __init__(self):
        self.items = []
        self.lock = Lock()

    def add_item(self, item):
        with self.lock:
            self.items.append(item)

    def remove_item(self, item):
        with self.lock:
            if item in self.items:
                self.items.remove(item)

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('apple')
    inventory.add_item('banana')
    print(inventory.items)
    inventory.remove_item('apple')
    print(inventory.items)