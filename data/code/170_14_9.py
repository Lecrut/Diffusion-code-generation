class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def remove_item(self, name, quantity):
        if name in self.items and self.items[name] >= quantity:
            self.items[name] -= quantity
            if self.items[name] == 0:
                del self.items[name]
        else:
            raise ValueError("Item not enough or does not exist")

    def display_inventory(self):
        print("--- Inventory ---")
        if not self.items:
            print("Inventory is empty.")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")
        print("-----------------")

if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Apples", 50)
    my_inventory.add_item("Bananas", 120)
    my_inventory.remove_item("Bananas", 60)
    my_inventory.display_inventory()