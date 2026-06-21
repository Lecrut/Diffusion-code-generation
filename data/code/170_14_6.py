class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not item_name.strip():
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not item_name.strip():
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
        else:
            raise ValueError("Insufficient inventory or invalid item name.")

    def list_inventory(self):
        print("--- Inventory ---")
        if not self.items:
            print("Inventory is empty.")
        for item, quantity in sorted(self.items.items()):
            print(f"{item}: {quantity}")
        print("-----------------")

if __name__ == '__main__':
    my_inventory = Inventory()
    try:
        my_inventory.add_item("Apples", 50)
        my_inventory.add_item("Bananas", 120)
        my_inventory.add_item("Oranges", 75)
        my_inventory.add_item("Grapes", 30)
        my_inventory.remove_item("Bananas", 60)
        my_inventory.list_inventory()
    except ValueError as e:
        print(e)