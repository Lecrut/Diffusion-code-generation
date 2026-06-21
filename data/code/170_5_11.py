class Inventory:

    def __init__(self):
        self.items = []

    def insert(self, item):
        index = self._binary_search(item)
        if index < len(self.items) and self.items[index].id == item.id:
            return False
        self.items.insert(index, item)
        return True

    def lookup(self, item_id):
        index = self._binary_search(item_id)
        if index < len(self.items) and self.items[index].id == item_id:
            return self.items[index]
        return None

    def _binary_search(self, key):
        low, high = (0, len(self.items) - 1)
        while low <= high:
            mid = (low + high) // 2
            if self.items[mid].id < key:
                low = mid + 1
            elif self.items[mid].id > key:
                high = mid - 1
            else:
                return mid
        return low

class Item:

    def __init__(self, id, name):
        self.id = id
        self.name = name
if __name__ == '__main__':
    inventory = Inventory()
    inventory.insert(Item(1, 'Apple'))
    inventory.insert(Item(3, 'Banana'))
    inventory.insert(Item(2, 'Cherry'))
    print(inventory.lookup(2).name)
    print(inventory.lookup(4))