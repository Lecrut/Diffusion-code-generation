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
    print(f"Value of apple: {manager.get_item('apple')}")
    print(f"Value of banana: {manager.get_item('banana')}")
    print(f"Value of grape: {manager.get_item('grape')}")