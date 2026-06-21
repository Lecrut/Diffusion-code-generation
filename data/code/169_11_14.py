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

    def check_availability(self, item):
        return self._inventory.get(item, 0) > 0

    @staticmethod
    def _to_json(data):
        json_str = ''
        for key, value in data.items():
            json_str += f'"{key}": {value}, '
        return json_str.rstrip(', ')

    def export_inventory(self):
        return '{' + self._to_json(self._inventory) + '}'
if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_item('apples', 30)
    manager.remove_item('apples', 15)
    print(manager.check_availability('apples'))
    print(manager.export_inventory())