class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name}: {self.quantity}"

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, quantity):
        new_item = Item(item_name, quantity)
        index = bisect.bisect_left(self.items, new_item, key=lambda x: x.name)
        if index < len(self.items) and self.items[index].name == item_name:
            self.items[index].quantity += quantity
        else:
            self.items.insert(index, new_item)

    def lookup_item(self, item_name):
        index = bisect.bisect_left(self.items, Item(item_name, 0), key=lambda x: x.name)
        if index < len(self.items) and self.items[index].name == item_name:
            return self.items[index]
        return None

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item("Apples", 50)
    inventory.add_item("Bananas", 120)
    inventory.add_item("Oranges", 75)
    inventory.add_item("Grapes", 30)
    inventory.add_item("Pears", 45)

    print(inventory.lookup_item("Oranges"))