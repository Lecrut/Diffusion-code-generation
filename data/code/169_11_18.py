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

    def check_availability(self, item):
        return self.items.get(item, 0)

    def export_inventory(self):
        import json
        return json.dumps(self.items)

if __name__ == '__main__':
    inventory = InventoryManager()
    inventory.add_item('apple', 10)
    inventory.add_item('banana', 5)
    print(inventory.check_availability('apple'))
    print(inventory.export_inventory())