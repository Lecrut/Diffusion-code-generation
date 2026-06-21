class ItemStore:
    def __init__(self):
        self.items = iter([
            "apple", "banana", "cherry", "date", "elderberry",
            "fig", "grape", "honeydew", "kiwi", "lemon"
        ])

    def get_next_item(self):
        try:
            return next(self.items)
        except StopIteration:
            raise ValueError("No more items available")

if __name__ == '__main__':
    store = ItemStore()
    print(store.get_next_item())
    print(store.get_next_item())
    print(store.get_next_item())
    print(store.get_next_item())
    print(store.get_next_item())
    print(store.get_next_item())
    print(store.get_next_item())
    print(store.get_next_item())
    print(store.get_next_item())
    print(store.get_next_item())