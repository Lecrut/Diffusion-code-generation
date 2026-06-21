class LargeItemStore:
    def __init__(self):
        self.items = iter([
            "apple", "banana", "cherry", "date", "elderberry",
            "fig", "grape", "honeydew", "kiwi", "lemon",
            "mango", "nectarine", "orange", "papaya", "quince",
            "raspberry", "strawberry", "tangerine", "ugli fruit", "vanilla bean"
        ])

    def get_next_item(self):
        try:
            return next(self.items)
        except StopIteration:
            return None

if __name__ == '__main__':
    store = LargeItemStore()
    print(store.get_next_item())
    print(store.get_next_item())
    print(store.get_next_item())