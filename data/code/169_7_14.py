class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def update_inventory(self, transactions):
        for item_name, quantity in transactions:
            if item_name not in self.inventory:
                self.inventory[item_name] = 0
            self.inventory[item_name] += quantity

    def get_inventory(self):
        return sorted((item, count) for item, count in self.inventory.items())

if __name__ == '__main__':
    manager = InventoryManager()
    transactions = [
        ('apple', 3),
        ('banana', -1),
        ('orange', 2),
        ('apple', 5)
    ]
    manager.update_inventory(transactions)
    print(manager.get_inventory())