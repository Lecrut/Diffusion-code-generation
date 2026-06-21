stores = [
    ("Store A", 25),
    ("Store B", 30),
    ("Store C", 22),
    ("Store D", 45)
]

def validate_stores(stores):
    if not all(isinstance(store, tuple) and len(store) == 2 for store in stores):
        raise ValueError("Invalid stores format")
    if not all(isinstance(store[0], str) and isinstance(store[1], int) for store in stores):
        raise ValueError("Store name must be a string and age must be an integer")

def print_stores(stores):
    validate_stores(stores)
    for store, age in stores:
        print(f'Store: {store}, Age: {age}')

if __name__ == '__main__':
    print_stores(stores)