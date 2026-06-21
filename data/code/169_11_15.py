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
            else:
                self._inventory[item] = 0

    def check_availability(self, item):
        return self._inventory.get(item, 0) > 0

    def export_inventory(self):
        import json
        return json.dumps(self._inventory)
if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_item('apple', 10)
    manager.remove_item('apple', 3)
    print(manager.check_availability('apple'))
    print(manager.export_inventory())