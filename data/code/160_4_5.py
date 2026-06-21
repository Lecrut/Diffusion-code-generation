import threading

class Inventory:
    def __init__(self):
        self.items = []
        self.lock = threading.Lock()

    def add_item(self, item):
        if not self.is_valid_add(item):
            return False
        with self.lock:
            self.items.append(item)
        return True

    def remove_item(self, item):
        if not self.is_valid_remove(item):
            return False
        with self.lock:
            self.items.remove(item)
        return True

    def is_valid_add(self, item):
        return item is not None and isinstance(item, str)

    def is_valid_remove(self, item):
        return item in self.items

if __name__ == '__main__':
    inventory = Inventory()
    if inventory.add_item('apple'):
        print("Apple added successfully")
    else:
        print("Failed to add apple")

    if inventory.add_item('banana'):
        print("Banana added successfully")
    else:
        print("Failed to add banana")

    print(inventory.items)

    if inventory.remove_item('apple'):
        print("Apple removed successfully")
    else:
        print("Failed to remove apple")

    print(inventory.items)