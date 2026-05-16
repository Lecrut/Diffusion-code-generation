class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
    def remove_item(self, item_name, quantity):
        if item_name not in self.items:
            return False
        if self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
            return True
        else:
            return False
    def list_items(self):
        return self.items
if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Apples", 50)
    my_inventory.add_item("Bananas", 100)
    my_inventory.add_item("Oranges", 75)
    print("Initial Inventory:")
    print(my_inventory.list_items())
    my_inventory.add_item("Apples", 20)
    print("\nAfter adding 20 Apples:")
    print(my_inventory.list_items())
    print("\nRemoving 10 Bananas:")
    success = my_inventory.remove_item("Bananas", 10)
    if success:
        print("Removal successful.")
    else:
        print("Removal failed (not enough items).")
    print(my_inventory.list_items())
    print("\nAttempting to remove too many Oranges:")
    success = my_inventory.remove_item("Oranges", 100)
    if success:
        print("Removal successful.")
    else:
        print("Removal failed (not enough items).")
    print(my_inventory.list_items())
    print("\nAttempting to remove non-existent item:")
    success = my_inventory.remove_item("Grapes", 5)
    if success:
        print("Removal successful.")
    else:
        print("Removal failed (item not found).")
    print(my_inventory.list_items())