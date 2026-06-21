class InventoryManager:
    def __init__(self):
        self.inventory = {}
    
    @staticmethod
    def process_transactions(transactions):
        manager = InventoryManager()
        for item, quantity in transactions:
            manager.add_item(item, quantity)
        return sorted(manager.get_inventory().items())
    
    def add_item(self, item_name, quantity):
        if quantity <= 0:
            return
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
    
    def get_inventory(self):
        return self.inventory

if __name__ == '__main__':
    transactions = [
        ('apple', 3),
        ('banana', 2),
        ('apple', -1),
        ('orange', 5)
    ]
    result = InventoryManager.process_transactions(transactions)
    print(result)