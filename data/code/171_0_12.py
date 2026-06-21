stores = [
    {"name": "Store A", "description": "A large store with many items."},
    {"name": "Store B", "description": "Small convenience store."},
    {"name": "Store C", "description": "Offers a variety of products."},
    {"name": "Store D", "description": "Discounts on electronics."},
    {"name": "Store E", "description": "Bakery and café."}
]

filtered_stores = [store for store in stores if len(store["description"]) >= 10]

if __name__ == '__main__':
    print(filtered_stores)