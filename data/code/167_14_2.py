stores = [
    {'name': 'Store X', 'age': 15},
    {'name': 'Store Y', 'age': 7},
    {'name': 'Store Z', 'age': 9}
]

def filter_stores(stores):
    return [store for store in stores if store['age'] > 10]

if __name__ == '__main__':
    filtered_stores = filter_stores(stores)
    print(filtered_stores)