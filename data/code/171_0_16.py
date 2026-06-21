stores = [
    {'name': 'Store A', 'description': 'A great store'},
    {'name': 'Store B', 'description': 'Good stuff'},
    {'name': 'Store C', 'description': 'Cheap and cheerful'}
]

filtered_stores = [store for store in stores if len(store['description']) >= 10]

if __name__ == '__main__':
    print(filtered_stores)