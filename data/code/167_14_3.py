stores = [
    {'name': 'Store A', 'age': 5},
    {'name': 'Store B', 'age': 12},
    {'name': 'Store C', 'age': 8}
]

class StoreFilter:
    MIN_AGE = 10

    @staticmethod
    def filter_stores(stores):
        return [store for store in stores if store['age'] > StoreFilter.MIN_AGE]

if __name__ == '__main__':
    filtered_stores = StoreFilter.filter_stores(stores)
    print(filtered_stores)