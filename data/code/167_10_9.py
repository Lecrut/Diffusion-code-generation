stores = [
    ("Store A", 5),
    ("Store B", 3),
    ("Store C", 8)
]

def print_stores_info(stores):
    for store, age in stores:
        print(f"Store: {store}, Age: {age}")

if __name__ == '__main__':
    print_stores_info(stores)