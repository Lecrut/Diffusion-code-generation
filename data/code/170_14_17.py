class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
        else:
            raise ValueError("Item not found or insufficient quantity")

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
    my_inventory.remove_item("Bananas", 30)
    my_inventory.display_inventory()