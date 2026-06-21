class InventoryManager:
    def __init__(self):
        self.items = {}

    def add_items(self, items: dict):
        for item, count in items.items():
            if item in self.items:
                self.items[item] += count
            else:
                self.items[item] = count

    def remove_items(self, item: str, quantity: int) -> bool:
        if item not in self.items or self.items[item] < quantity:
            return False
        self.items[item] -= quantity
        if self.items[item] == 0:
            del self.items[item]
        return True

    def check_critical_threshold(self, threshold: int):
        for item, count in self.items.items():
            if count <= threshold:
                print(f"Critical threshold reached for {item}: {count}")

if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_items({"Apple": 10, "Banana": 5, "Orange": 8})
    manager.remove_items("Apple", 3)
    manager.check_critical_threshold(2)