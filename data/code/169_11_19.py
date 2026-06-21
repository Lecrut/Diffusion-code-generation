class InventoryManager:
    def __init__(self):
        self._inventory = {}

    def add_item(self, item, amount):
        if item in self._inventory:
            self._inventory[item] += amount
        else:
            self._inventory[item] = amount

    def remove_item(self, item, amount):
        if item in self._inventory and self._inventory[item] >= amount:
            self._inventory[item] -= amount
        elif item in self._inventory:
            self._inventory[item] = 0

    def is_available(self, item, amount):
        return item in self._inventory and self._inventory[item] >= amount

    @staticmethod
    def _to_json(data):
        if isinstance(data, dict):
            return '{' + ', '.join(f'"{k}": {InventoryManager._to_json(v)}' for k, v in data.items()) + '}'
        elif isinstance(data, list):
            return '[' + ', '.join(InventoryManager._to_json(item) for item in data) + ']'
        else:
            return str(data)

    def to_json(self):
        return InventoryManager._to_json(self._inventory)

if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_item('apples', 10)
    manager.remove_item('apples', 3)
    print(manager.is_available('apples', 5))
    print(manager.to_json())