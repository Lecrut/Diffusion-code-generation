stores = [
    ("Store A", 3),
    ("Store B", 5),
    ("Store C", 2)
]

def print_stores(stores):
    for store, age in stores:
        print(f"Store: {store}, Age: {age}")

if __name__ == '__main__':
    print_stores(stores)