stores = [
    ("Store A", 25),
    ("Store B", 30),
    ("Store C", 22),
    ("Store D", 45)
]

def print_stores(stores):
    for store, age in stores:
        print(f'Store: {store}, Age: {age}')

if __name__ == '__main__':
    try:
        if not all(isinstance(store, tuple) and len(store) == 2 for store in stores):
            raise ValueError("Invalid input format")
        print_stores(stores)
    except Exception as e:
        print(f"Error: {e}")