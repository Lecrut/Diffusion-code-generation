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
    inventory.add_item(102, "Mouse", 10)
    inventory.add_item(103, "Keyboard", 8)
    inventory.add_item(104, "Monitor", 3)
    print("Searching for 'Laptop':")
    print(inventory.search_items("Laptop"))
    print("\nSearching for 'Mouse':")
    print(inventory.search_items("Mouse"))
    print("\nSearching for ID '102':")
    print(inventory.search_items("102"))
    print("\nSearching for partial name 'Key':")
    print(inventory.search_items("Key"))
    print("\nSearching for non-existent item 'MonitorX':")
    print(inventory.search_items("MonitorX"))