def sort_stores_by_description_length(store_list):
    return sorted(store_list, key=lambda store: len(store['description']), reverse=True)
if __name__ == '__main__':
    store_data = [
        {'name': 'Store A', 'description': 'A small shop'},
        {'name': 'Store B', 'description': 'A very long and detailed description'},
        {'name': 'Store C', 'description': 'Medium size store'},
        {'name': 'Store D', 'description': 'Short description'}
    ]
    sorted_data = sort_stores_by_description_length(store_data)
    print(sorted_data)