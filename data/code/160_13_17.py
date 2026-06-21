class InventoryInitializer:
    DEFAULT_QUANTITY = 1

    @staticmethod
    def initialize_inventory(item_names):
        return {item: InventoryInitializer.DEFAULT_QUANTITY for item in set(item_names)}

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    inventory = InventoryInitializer.initialize_inventory(sample_items)
    print(inventory)