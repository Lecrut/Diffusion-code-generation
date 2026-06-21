stores = [
    {'name': 'Store A', 'description': 'A great store with a wide variety of products.'},
    {'name': 'Store B', 'description': 'Small local store.'},
    {'name': 'Store C', 'description': 'Large supermarket with everything you need.'}
]

filtered_stores = [store for store in stores if len(store['description']) >= 10]

if __name__ == '__main__':
    print(filtered_stores)