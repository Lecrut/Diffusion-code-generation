STORES = [
    ("Store A", 25),
    ("Store B", 30),
    ("Store C", 22),
    ("Store D", 45)
]

def format_store_entry(store, age):
    return f'Store: {store}, Age: {age}'

if __name__ == '__main__':
    for store, age in STORES:
        print(format_store_entry(store, age))