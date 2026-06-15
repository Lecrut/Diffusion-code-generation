def sort_stores_by_description_length(stores):
    return sorted(stores, key=lambda store: len(store['description']), reverse=True)
if __name__ == '__main__':
    store_data = [
        {'name': 'Store A', 'description': 'A small shop'},
        {'name': 'Store B', 'description': 'A very long and detailed description for this store'},
        {'name': 'Store C', 'description': 'Medium sized place'},
        {'name': 'Store D', 'description': 'Short entry'}
    ]
    sorted_stores = sort_stores_by_description_length(store_data)
    print(sorted_stores)