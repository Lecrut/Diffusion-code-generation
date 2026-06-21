class Item:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __lt__(self, other):
        return self.name < other.name

class Inventory:

    def __init__(self):
        self.items = []

    def add_item(self, item_name, quantity):
        new_item = Item(item_name, quantity)
        index = self._binary_search(new_item)
        if index >= 0:
            self.items[index].quantity += quantity
        else:
            self.items.insert(-(index + 1), new_item)

    def lookup_item(self, item_name):
        index = self._binary_search(Item(item_name, 0))
        if index >= 0:
            return self.items[index].quantity
        return None

    def _binary_search(self, item):
        low, high = (0, len(self.items) - 1)
        while low <= high:
            mid = (low + high) // 2
            if self.items[mid] < item:
                low = mid + 1
            elif self.items[mid] > item:
                high = mid - 1
            else:
                return mid
        return -(low + 1)
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('Apples', 50)
    inventory.add_item('Bananas', 120)
    inventory.add_item('Oranges', 75)
    inventory.add_item('Grapes', 30)
    inventory.add_item('Pears', 45)
    print(inventory.lookup_item('Bananas'))
    print(inventory.lookup_item('Mangoes'))