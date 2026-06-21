stores = {
    "Store A": 25,
    "Store B": 30,
    "Store C": 22,
    "Store D": 45
}

def print_stores(stores):
    for store, age in stores.items():
        print(f'Store: {store}, Age: {age}')

if __name__ == '__main__':
    print_stores(stores)