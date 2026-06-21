class InventoryManager:
    def __init__(self):
        self.items = {}

    def add_item(self, item, count):
        if item in self.items:
            self.items[item] += count
        else:
            self.items[item] = count

    def remove_item(self, item, count):
        if item in self.items and self.items[item] >= count:
            self.items[item] -= count
            if self.items[item] == 0:
                del self.items[item]
        else:
            raise ValueError("Not enough items or item does not exist")

    def check_availability(self, item):
        return self.items.get(item, 0)

    def export_inventory(self):
        import json
        return json.dumps(self.items)

if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_item('apple', 10)
    manager.add_item('banana', 5)
    print(manager.check_availability('apple'))
    manager.remove_item('apple', 3)
    print(manager.export_inventory())