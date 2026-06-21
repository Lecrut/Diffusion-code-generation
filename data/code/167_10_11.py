class StoreData:
    def __init__(self):
        self.stores = [
            ("Store A", 25),
            ("Store B", 30),
            ("Store C", 22),
            ("Store D", 45)
        ]

    def print_stores(self):
        for store, age in self.stores:
            print(f'Store: {store}, Age: {age}')

if __name__ == '__main__':
    store_data = StoreData()
    store_data.print_stores()