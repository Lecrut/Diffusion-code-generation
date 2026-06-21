stores = [
    {'name': 'Store A', 'age': 15},
    {'name': 'Store B', 'age': 8},
    {'name': 'Store C', 'age': 12}
]

def filter_stores(stores):
    return [store for store in stores if store['age'] > 10]

if __name__ == '__main__':
    filtered_stores = filter_stores(stores)
    print(filtered_stores)