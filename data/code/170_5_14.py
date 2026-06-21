class Inventory:

    def __init__(self):
        self.items = []

    def insert(self, item):
        left, right = (0, len(self.items))
        while left < right:
            mid = (left + right) // 2
            if self.items[mid].id < item.id:
                left = mid + 1
            else:
                right = mid
        self.items.insert(left, item)

    def lookup(self, item_id):
        left, right = (0, len(self.items))
        while left < right:
            mid = (left + right) // 2
            if self.items[mid].id == item_id:
                return self.items[mid]
            elif self.items[mid].id < item_id:
                left = mid + 1
            else:
                right = mid
        raise ValueError('Item not found')

class Item:

    def __init__(self, id, name):
        self.id = id
        self.name = name
if __name__ == '__main__':
    inventory = Inventory()
    inventory.insert(Item(3, 'C'))
    inventory.insert(Item(1, 'A'))
    inventory.insert(Item(2, 'B'))
    print(inventory.lookup(2).name)