class ItemStore:
    def __init__(self):
        self.items = (
            "apple", "banana", "cherry", "date", "elderberry",
            "fig", "grape", "honeydew", "kiwi", "lemon",
            "mango", "nectarine", "orange", "papaya", "quince",
            "raspberry", "strawberry", "tangerine", "ugli fruit", "vanilla bean"
        )

    def __iter__(self):
        for item in self.items:
            yield item

if __name__ == '__main__':
    store = ItemStore()
    print(next(store))
    print(next(store))