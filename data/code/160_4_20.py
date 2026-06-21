import threading

class Inventory:
    ADD_ITEM_LOCK = threading.Lock()
    REMOVE_ITEM_LOCK = threading.Lock()

    def __init__(self):
        self.items = []

    @staticmethod
    def _is_item_in_inventory(item, inventory):
        return item in inventory.items

    def add_item(self, item):
        with self.ADD_ITEM_LOCK:
            if not self._is_item_in_inventory(item, self):
                self.items.append(item)

    def remove_item(self, item):
        with self.REMOVE_ITEM_LOCK:
            if self._is_item_in_inventory(item, self):
                self.items.remove(item)

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('apple')
    inventory.add_item('banana')
    print(inventory.items)
    inventory.remove_item('apple')
    print(inventory.items)