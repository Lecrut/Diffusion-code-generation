class InventoryManager:
    def __init__(self):
        self.inventory = []

    def insert_item(self, item_id, count):
        if not isinstance(item_id, int) or not isinstance(count, (int, float)):
            raise ValueError("Invalid item ID or count")
        count = int(count)
        while len(self.inventory) <= item_id:
            self.inventory.append(0)
        self.inventory[item_id] += count

    def update_item(self, item_id, count):
        if not isinstance(item_id, int) or not isinstance(count, (int, float)):
            raise ValueError("Invalid item ID or count")
        count = int(count)
        if 0 <= item_id < len(self.inventory):
            self.inventory[item_id] += count
        else:
            raise IndexError("Item ID out of range")

    def delete_item(self, item_id):
        if not isinstance(item_id, int):
            raise ValueError("Invalid item ID")
        if 0 <= item_id < len(self.inventory):
            del self.inventory[item_id]

if __name__ == '__main__':
    manager = InventoryManager()
    manager.insert_item(0, 10)
    manager.update_item(0, 5)
    manager.insert_item(1, 20)
    manager.delete_item(0)
    print(manager.inventory)