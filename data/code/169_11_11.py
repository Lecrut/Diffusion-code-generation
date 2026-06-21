class InventoryManager:
    def __init__(self):
        self._inventory = {}
    
    def add_item(self, item, amount):
        if item in self._inventory:
            self._inventory[item] += amount
        else:
            self._inventory[item] = amount
    
    def remove_item(self, item, amount):
        if item in self._inventory:
            if self._inventory[item] >= amount:
                self._inventory[item] -= amount
            elif self._inventory[item] > 0:
                self._inventory[item] = 0
            else:
                del self._inventory[item]
    
    def is_available(self, item, amount):
        return self._inventory.get(item, 0) >= amount
    
    def to_json(self):
        import json
        return json.dumps(self._inventory, indent=4)

if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_item("apple", 15)
    manager.remove_item("apple", 5)
    print(manager.is_available("apple", 7))
    print(manager.to_json())