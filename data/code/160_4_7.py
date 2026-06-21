import threading

class Inventory:
    ITEM_ADD_ERROR = 'Item already exists'
    ITEM_REMOVE_ERROR = 'Item does not exist'

    def __init__(self):
        self.items = []
        self.lock = threading.Lock()

    def add_item(self, item):
        with self.lock:
            if item in self.items:
                raise ValueError(self.ITEM_ADD_ERROR)
            self.items.append(item)

    def remove_item(self, item):
        with self.lock:
            if item not in self.items:
                raise ValueError(self.ITEM_REMOVE_ERROR)
            self.items.remove(item)

if __name__ == '__main__':
    inventory = Inventory()
    try:
        inventory.add_item('apple')
        print(inventory.items)
        inventory.add_item('banana')
        print(inventory.items)
        inventory.remove_item('apple')
        print(inventory.items)
        inventory.remove_item('banana')
        print(inventory.items)
    except ValueError as e:
        print(e)