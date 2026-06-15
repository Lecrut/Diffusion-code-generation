def sort_stores_by_description_length(store_list):
    return sorted(store_list, key=lambda store: len(store['description']), reverse=True)
if __name__ == '__main__':
    stores = [
        {'name': 'Store A', 'description': 'A small shop.'},
        {'name': 'Store B', 'description': 'A very long and detailed description for this store.'},
        {'name': 'Store C', 'description': 'Medium length description.'},
        {'name': 'Store D', 'description': 'Short'},
        {'name': 'Store E', 'description': 'Another slightly longer one.'}
    ]
    sorted_stores = sort_stores_by_description_length(stores)
    print(sorted_stores)