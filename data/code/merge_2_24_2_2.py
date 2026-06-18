class InventoryManager:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_id, name, quantity):
        if item_id in self.inventory:
            current_qty = self.inventory[item_id]['quantity']
            self.inventory[item_id]['quantity'] += quantity
        else:
            self.inventory[item_id] = {'name': name, 'quantity': quantity}
    def remove_item(self, item_id, amount):
        if item_id in self.inventory and self.inventory[item_id]['quantity'] >= amount:
            self.inventory[item_id]['quantity'] -= amount
            return True
        else:
            del self.inventory[item_id]
            return False
    def search_by_name(self, name_pattern):
        results = []
        for item in self.inventory.values():
            if name_pattern.lower() in item['name'].lower():
                results.append(item)
        return results
if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_item('001', 'Laptop', 5)
    manager.add_item('002', 'Mouse', 20)
    manager.add_item('003', 'Keyboard', 10)
    manager.add_item('004', 'Monitor', 8)
    found = manager.search_by_name("Key")
    print(f"Items matching \"Key\": {found}")
    removed = manager.remove_item('002', 5)
    if removed:
        current_qty = manager.inventory['002']['quantity']
        print(f"Removed 5 Mice. Remaining quantity for 'Mouse': {current_qty}")