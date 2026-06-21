STORES = [
    {'name': 'Store A', 'age': 5},
    {'name': 'Store B', 'age': 12},
    {'name': 'Store C', 'age': 8}
]

def filter_stores(stores):
    return [store for store in stores if store['age'] > 10]

if __name__ == '__main__':
    filtered_stores = filter_stores(STORES)
    print(filtered_stores)