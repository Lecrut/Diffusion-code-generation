import threading

class Inventory:
    def __init__(self):
        self.items = []
        self.lock = threading.Lock()

    def add_item(self, item):
        with self.lock:
            if not self.is_item_present(item):
                self.items.append(item)

    def remove_item(self, item):
        with self.lock:
            if self.is_item_present(item):
                self.items.remove(item)

    def is_item_present(self, item):
        return item in self.items

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('apple')
    inventory.add_item('banana')
    print(inventory.items)
    inventory.remove_item('apple')
    print(inventory.items)