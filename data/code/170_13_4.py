class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, item_id, name, quantity):
        self.items[item_id] = {"name": name, "quantity": quantity}
    def search_items(self, query):
        results = []
        if not query:
            return results
        query_lower = query.lower()
        for item_id, data in self.items.items():
            item_name = data["name"].lower()
            item_id_str = str(item_id).lower()
            if query_lower in item_name or query_lower in item_id_str:
                results.append({"id": item_id, "name": data["name"], "quantity": data["quantity"]})
        return results
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item(101, "Laptop", 5)
    inventory.add_item(202, "Mouse", 10)
    inventory.add_item(303, "Keyboard", 8)
    inventory.add_item(404, "Monitor", 3)
    print("Searching for items containing 'Laptop':")
    print(inventory.search_items("Laptop"))
    print("\nSearching for items containing 'Mouse':")
    print(inventory.search_items("Mouse"))
    print("\nSearching for items containing '101':")
    print(inventory.search_items("101"))
    print("\nSearching for items containing 'Keyb':")
    print(inventory.search_items("Keyb"))
    print("\nSearching for non-existent item 'MonitorX':")
    print(inventory.search_items("MonitorX"))