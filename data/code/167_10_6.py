class StoreInfo:
    STORES = [
        ("Store A", 25),
        ("Store B", 30),
        ("Store C", 22),
        ("Store D", 45)
    ]

    @staticmethod
    def print_stores():
        for store, age in StoreInfo.STORES:
            print(f'Store: {store}, Age: {age}')

if __name__ == '__main__':
    StoreInfo.print_stores()