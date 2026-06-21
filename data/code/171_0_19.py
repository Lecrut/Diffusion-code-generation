stores = [
    {"name": "Store A", "description": "A variety store."},
    {"name": "Store B", "description": "Electronics and gadgets."},
    {"name": "Store C", "description": "Home decor items."},
    {"name": "Store D", "description": "Books and stationery."},
]

filtered_stores = [store for store in stores if len(store["description"]) >= 10]

if __name__ == '__main__':
    print(filtered_stores)