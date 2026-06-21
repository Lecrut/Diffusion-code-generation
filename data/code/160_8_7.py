class ItemStore:
    def __init__(self):
        self.items = (
            "apple", "banana", "cherry", "date", "elderberry",
            "fig", "grape", "honeydew", "kiwi", "lemon",
            "mango", "nectarine", "orange", "papaya", "quince",
            "raspberry", "strawberry", "tangerine", "ugli fruit", "vanilla bean"
        )

    def __iter__(self):
        return iter(self.items)

if __name__ == '__main__':
    store = ItemStore()
    for item in store:
        print(item)