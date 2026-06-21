class StoreAgeFormatter:
    def __init__(self):
        self.stores = [
            ("Store A", 25),
            ("Store B", 30),
            ("Store C", 22),
            ("Store D", 45)
        ]

    def format_stores(self):
        for store, age in self.stores:
            print(f'Store: {store}, Age: {age}')

if __name__ == '__main__':
    formatter = StoreAgeFormatter()
    formatter.format_stores()