class Item:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Inventory:

    def __init__(self):
        self.items = []

    def _binary_search(self, item_name):
        low = 0
        high = len(self.items) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.items[mid].name == item_name:
                return mid
            elif self.items[mid].name < item_name:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def add_item(self, item_name, quantity):
        index = self._binary_search(item_name)
        if index != -1:
            self.items[index].quantity += quantity
        else:
            insert_index = self._binary_search(item_name) * -1 - 1
            new_item = Item(item_name, quantity)
            self.items.insert(insert_index, new_item)

    def get_quantity(self, item_name):
        index = self._binary_search(item_name)
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
    print(inventory.get_quantity('Oranges'))
    print(inventory.get_quantity('Bananas'))
    print(inventory.get_quantity('Watermelons'))