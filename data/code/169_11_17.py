class InventoryManager:
    def __init__(self):
        self._inventory = {}

    def add_item(self, item: str, count: int) -> None:
        if not isinstance(item, str) or not isinstance(count, int):
            raise ValueError("Item must be a string and count must be an integer")
        if count < 0:
            raise ValueError("Count cannot be negative")
        self._inventory[item] = self._inventory.get(item, 0) + count

    def remove_item(self, item: str, count: int) -> None:
        if not isinstance(item, str) or not isinstance(count, int):
            raise ValueError("Item must be a string and count must be an integer")
        if count < 0:
            raise ValueError("Count cannot be negative")
        if item in self._inventory:
            if self._inventory[item] >= count:
                self._inventory[item] -= count
            else:
                del self._inventory[item]

    def is_available(self, item: str) -> bool:
        if not isinstance(item, str):
            raise ValueError("Item must be a string")
        return item in self._inventory

    def export_inventory(self) -> str:
        return str(self._inventory)

if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_item("apple", 3)
    manager.remove_item("apple", 1)
    print(manager.is_available("apple"))
    print(manager.export_inventory())