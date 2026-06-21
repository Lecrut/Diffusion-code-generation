stores = [
    {'name': 'Store Alpha', 'age': 15},
    {'name': 'Store Beta', 'age': 9},
    {'name': 'Store Gamma', 'age': 7}
]

def filter_stores(stores):
    return [store for store in stores if store['age'] > 10]

if __name__ == '__main__':
    filtered_stores = filter_stores(stores)
    print(filtered_stores)