class Inventory:
    def __init__(self):
        self.items = []
    
    def _binary_search(self, item_name):
        low, high = 0, len(self.items) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.items[mid][0] == item_name:
                return mid
            elif self.items[mid][0] < item_name:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    def add_item(self, item_name, quantity):
        index = self._binary_search(item_name)
        if index != -1:
            self.items[index][1] += quantity
        else:
            self.items.insert(index, [item_name, quantity])
    
    def lookup_item(self, item_name):
        index = self._binary_search(item_name)
        return self.items[index][1] if index != -1 else None
    
    def list_inventory(self):
        for item in self.items:
            print(f"{item[0]}: {item[1]}")

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item("Apples", 50)
    inventory.add_item("Bananas", 120)
    inventory.add_item("Oranges", 75)
    inventory.add_item("Grapes", 30)
    inventory.add_item("Pears", 45)
    
    print(f"Inventory Lookup for Apples: {inventory.lookup_item('Apples')}")
    print(f"Inventory Lookup for Oranges: {inventory.lookup_item('Oranges')}")
    inventory.list_inventory()