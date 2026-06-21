stores = [
    ("Store X", 15),
    ("Store Y", 25),
    ("Store Z", 35)
]

def print_store_info(stores):
    for store, age in stores:
        print(f'Store: {store}, Age: {age}')

if __name__ == '__main__':
    print_store_info(stores)