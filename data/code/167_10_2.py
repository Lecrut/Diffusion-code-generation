stores = [
    ("Store A", 2),
    ("Store B", 5),
    ("Store C", 3)
]

def print_stores(stores):
    for store, age in stores:
        print(f"Store: {store}, Age: {age}")

if __name__ == '__main__':
    print_stores(stores)