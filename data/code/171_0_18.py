class StoreFilter:
    MIN_DESCRIPTION_LENGTH = 10

    @staticmethod
    def filter_stores(stores):
        return [store for store in stores if len(store['description']) >= StoreFilter.MIN_DESCRIPTION_LENGTH]

if __name__ == '__main__':
    sample_stores = [
        {'name': 'Store A', 'description': 'This is a short description.'},
        {'name': 'Store B', 'description': 'A longer description of the store.'}
    ]
    filtered_stores = StoreFilter.filter_stores(sample_stores)
    print(filtered_stores)