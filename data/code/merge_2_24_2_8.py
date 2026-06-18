class InventoryManager:
    def __init__(self):
        self.items = {}
    def add_item(self, item_id, name, quantity):
        if item_id in self.items:
            current_qty = self.items[item_id]['quantity']
            self.items[item_id] = {'name': name, 'quantity': current_qty + quantity}
        else:
            self.items[item_id] = {'name': name, 'quantity': quantity}
    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
        return True
    def search_items(self, keyword):
        results = []
        for item_id, data in self.items.items():
            if keyword.lower() in data['name'].lower():
                results.append(item_id)
        return results
if __name__ == '__main__':
    inv_mgr = InventoryManager()
    inv_mgr.add_item("I001", "Laptop", 5)
    inv_mgr.add_item("I002", "Mouse", 20)
    inv_mgr.add_item("I003", "Keyboard", 10)
    print(f"Total items: {len(inv_mgr.items)}")
    found_ids = inv_mgr.search_items("key")
    if found_ids:
        for id in found_ids:
            print(f"Found item ID: {id}")
    removed = inv_mgr.remove_item("I002")
    print(f"Removed I002: {removed}")