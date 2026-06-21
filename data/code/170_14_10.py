class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] > quantity:
                self.items[item_name] -= quantity
            elif self.items[item_name] == quantity:
                del self.items[item_name]
            else:
                raise ValueError("Not enough quantity to remove")
        else:
            raise KeyError(f"Item '{item_name}' not found")

    def display_inventory(self):
        print("--- Inventory ---")
        if not self.items:
            print("Inventory is empty.")
        for item, quantity in sorted(self.items.items()):
            print(f"{item}: {quantity}")
        print("-----------------")

if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Apples", 50)
    my_inventory.add_item("Bananas", 120)
    my_inventory.add_item("Oranges", 75)
    my_inventory.add_item("Grapes", 30)
    print("--- Initial Inventory State ---")
    my_inventory.display_inventory()
    try:
        my_inventory.remove_item("Apples", 30)
        print("\n--- After Removing Apples ---")
        my_inventory.display_inventory()
    except Exception as e:
        print(f"Error: {e}")