def initialize_inventory(item_names):
    return {item: 1 for item in set(item_names)}

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    inventory_manager = InventoryManager(sample_items)
    print(inventory_manager.get_inventory())
    print(inventory_manager.add_item('grape'))
    print(inventory_manager.get_inventory())

class InventoryManager:
    def __init__(self, item_names):
        self.inventory = initialize_inventory(item_names)

    def get_inventory(self):
        return self.inventory

    def add_item(self, item_name):
        if item_name not in self.inventory:
            self.inventory[item_name] = 1
        else:
            self.inventory[item_name] += 1
        return self.inventory