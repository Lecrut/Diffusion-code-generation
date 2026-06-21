stores = [
    ("Store A", 5),
    ("Store B", 3),
    ("Store C", 8)
]

def print_stores(stores):
    for store in stores:
        print(f"Store: {store[0]}, Age: {store[1]}")

if __name__ == '__main__':
    print_stores(stores)