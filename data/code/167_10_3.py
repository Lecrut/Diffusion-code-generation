stores = [
    ("Store A", 10),
    ("Store B", 20),
    ("Store C", 30)
]

def format_store_entry(store, age):
    return f'Store: {store}, Age: {age}'

if __name__ == '__main__':
    for store, age in stores:
        entry = format_store_entry(store, age)
        print(entry)