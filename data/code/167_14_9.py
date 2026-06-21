STores = [
    {'name': 'Store A', 'age': 5},
    {'name': 'Store B', 'age': 12},
    {'name': 'Store C', 'age': 8}
]

MIN_AGE = 10

def filter_stores(stores):
    return [store for store in stores if store['age'] > MIN_AGE]

if __name__ == '__main__':
    filtered_stores = filter_stores(STores)
    print(filtered_stores)