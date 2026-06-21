class Inventory:

    class Item:

        def __init__(self, name, quantity):
            self.name = name
            self.quantity = quantity

        def __eq__(self, other):
            return self.name == other.name and self.quantity == other.quantity

        def __lt__(self, other):
            return self.name < other.name
    ITEMS_KEY = 'items'

    def __init__(self):
        self.items = []

    @staticmethod
    def _binary_search(items, target):
        low, high = (0, len(items) - 1)
        while low <= high:
            mid = (low + high) // 2
            if items[mid] == target:
                return mid
            elif items[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def add_item(self, item_name, quantity):
        item = Inventory.Item(item_name, quantity)
        index = self._binary_search(self.items, item)
        if index != -1:
            self.items[index].quantity += quantity
        else:
            self.items.insert(bisect.bisect_left(self.items, item), item)

    def lookup_item(self, item_name):
        item = Inventory.Item(item_name, 0)
        index = self._binary_search(self.items, item)
        if index != -1:
            return self.items[index].quantity
        else:
            return None
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('Apples', 50)
    inventory.add_item('Bananas', 120)
    inventory.add_item('Oranges', 75)
    inventory.add_item('Grapes', 30)
    inventory.add_item('Pears', 45)
    print(inventory.lookup_item('Apples'))
    print(inventory.lookup_item('Bananas'))
    print(inventory.lookup_item('Oranges'))
    print(inventory.lookup_item('Grapes'))
    print(inventory.lookup_item('Pears'))
    print(inventory.lookup_item('Watermelons'))