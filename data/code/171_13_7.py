def sort_stores(store_list):
    return sorted(store_list, key=lambda store: len(store['description']), reverse=True)
if __name__ == '__main__':
    stores = [
        {'name': 'Store A', 'description': 'A small shop'},
        {'name': 'Store B', 'description': 'A very long and detailed description of this store'},
        {'name': 'Store C', 'description': 'Medium description'},
        {'name': 'Store D', 'description': 'Short'},
    ]
    sorted_stores = sort_stores(stores)
    print(sorted_stores)