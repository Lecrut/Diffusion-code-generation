class InventoryItem:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Inventory:

    def __init__(self):
        self.items = []

    def add_item(self, item_name, quantity):
        new_item = InventoryItem(item_name, quantity)
        index = self._binary_search(item_name)
        if index < len(self.items) and self.items[index].name == item_name:
            self.items[index].quantity += quantity
        else:
            self.items.insert(index, new_item)

    def _binary_search(self, item_name):
        left, right = (0, len(self.items) - 1)
        while left <= right:
            mid = (left + right) // 2
            if self.items[mid].name < item_name:
                left = mid + 1
            elif self.items[mid].name > item_name:
                right = mid - 1
            else:
                return mid
        return left

    def lookup_item(self, item_name):
        index = self._binary_search(item_name)
        if index < len(self.items) and self.items[index].name == item_name:
            return self.items[index].quantity
        return None
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('Apples', 50)
    inventory.add_item('Bananas', 120)
    inventory.add_item('Oranges', 75)
    inventory.add_item('Grapes', 30)
    inventory.add_item('Pears', 45)
    print(inventory.lookup_item('Bananas'))
    print(inventory.lookup_item('Grapes'))
    print(inventory.lookup_item('Mangoes'))