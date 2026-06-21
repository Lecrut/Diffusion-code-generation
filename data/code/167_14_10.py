def filter_stores(stores):
    return [store for store in stores if store['age'] > 10]

if __name__ == '__main__':
    stores = [
        {'name': 'Store A', 'age': 5},
        {'name': 'Store B', 'age': 12},
        {'name': 'Store C', 'age': 8}
    ]
    filtered_stores = filter_stores(stores)
    print(filtered_stores)