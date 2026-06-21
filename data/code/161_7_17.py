class ItemManager:
    def __init__(self):
        self.items = {}

    def add_item(self, key, value):
        self.items[key] = value

    def get_item(self, key):
        return self.items.get(key)

if __name__ == '__main__':
    manager = ItemManager()
    manager.add_item("apple", 100)
    manager.add_item("banana", 150)
    manager.add_item("cherry", 200)
    apple_price = manager.get_item("apple")
    banana_price = manager.get_item("banana")
    grape_price = manager.get_item("grape") or "Not found"
    print(f"Price of apple: {apple_price}")
    print(f"Price of banana: {banana_price}")
    print(f"Price of grape: {grape_price}")