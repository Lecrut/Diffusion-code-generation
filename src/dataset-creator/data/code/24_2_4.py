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
                results.append({'item_id': item_id, 'name': data['name'], 'quantity': data['quantity']})
        return results
    def get_total_quantity(self):
        total = sum(item['quantity'] for item in self.items.values())
        return total
if __name__ == '__main__':
    inv = InventoryManager()
    inv.add_item('A001', 'Laptop', 5)
    inv.add_item('B002', 'Mouse', 30)
    inv.add_item('C003', 'Keyboard', 15)
    print("Total Quantity:", inv.get_total_quantity())
    found = inv.search_items('key')
    if found:
        for item in found:
            print(f"Found {item['name']} (ID: {item['item_id']}, Qty: {item['quantity']})")
    inv.remove_item('B002')
    print("Removed B002. Remaining items:", len(inv.items))