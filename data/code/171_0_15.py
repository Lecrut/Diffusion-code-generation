stores = [
    {"name": "Store A", "description": "A great store."},
    {"name": "Store B", "description": "Good."},
    {"name": "Store C", "description": "Excellent, with lots of items!"},
    {"name": "Store D", "description": ""}
]

filtered_stores = [store for store in stores if len(store["description"]) >= 10]

if __name__ == '__main__':
    print(filtered_stores)