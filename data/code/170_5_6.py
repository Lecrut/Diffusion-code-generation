class Inventory:

    def __init__(self):
        self.items = []

    def insert(self, item):
        index = self._binary_search(item)
        if index < len(self.items) and self.items[index].id == item.id:
            return False
        self.items.insert(index, item)
        return True

    def _binary_search(self, item):
        low, high = (0, len(self.items))
        while low < high:
            mid = (low + high) // 2
            if self.items[mid].id < item.id:
                low = mid + 1
            else:
                high = mid
        return low

    def lookup(self, item_id):
        index = self._binary_search(Item(item_id))
        if index < len(self.items) and self.items[index].id == item_id:
            return self.items[index]
        return None

class Item:

    def __init__(self, id):
        self.id = id
if __name__ == '__main__':
    inventory = Inventory()
    inventory.insert(Item(10))
    inventory.insert(Item(20))
    inventory.insert(Item(30))
    print(inventory.lookup(20).id)
    print(inventory.lookup(40))