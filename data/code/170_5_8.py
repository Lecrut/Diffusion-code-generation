class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

def binary_search(items, target_name):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid].name == target_name:
            return mid
        elif items[mid].name < target_name:
            low = mid + 1
        else:
            high = mid - 1
    return -1

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, quantity):
        new_item = Item(item_name, quantity)
        index = binary_search(self.items, item_name)
        if index != -1:
            self.items[index].quantity += quantity
        else:
            self.items.insert(bisect.bisect_left(self.items, new_item), new_item)

    def lookup_item(self, item_name):
        index = binary_search(self.items, item_name)
        if index != -1:
            return f"{item_name}: {self.items[index].quantity}"
        else:
            return "Item not found"

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item("Apples", 50)
    inventory.add_item("Bananas", 120)
    inventory.add_item("Oranges", 75)
    inventory.add_item("Grapes", 30)
    inventory.add_item("Pears", 45)

    print(inventory.lookup_item("Apples"))
    print(inventory.lookup_item("Bananas"))
    print(inventory.lookup_item("Oranges"))
    print(inventory.lookup_item("Grapes"))
    print(inventory.lookup_item("Pears"))
    print(inventory.lookup_item("Strawberries"))