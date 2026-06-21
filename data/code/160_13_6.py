def initialize_inventory(item_names):
    return {item: 1 for item in set(item_names)}

class InventoryManager:
    def __init__(self, items):
        self.inventory = initialize_inventory(items)

    def get_inventory(self):
        return self.inventory

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    manager = InventoryManager(sample_items)
    print(manager.get_inventory())