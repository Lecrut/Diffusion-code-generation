stores = [
    {'name': 'Store A', 'description': 'A great store with lots of items.'},
    {'name': 'Store B', 'description': 'Small store.'},
    {'name': 'Store C', 'description': 'Another store with a variety of products.'}
]

filtered_stores = [store for store in stores if len(store['description']) >= 10]

if __name__ == '__main__':
    print(filtered_stores)