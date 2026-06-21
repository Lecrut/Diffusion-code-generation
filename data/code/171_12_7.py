def initialize_stores():
    return [
        {'name': 'Store A', 'description': 'Description for Store A'},
        {'name': 'Store B', 'description': 'Description for Store B'},
        {'name': 'Store C', 'description': 'Description for Store C'}
    ]

def update_store_description(stores, name, new_description):
    for store in stores:
        if store['name'] == name:
            store['description'] = new_description
            break

def get_stores_sorted_by_name(stores):
    return sorted(stores, key=lambda x: x['name'])

if __name__ == '__main__':
    stores = initialize_stores()
    update_store_description(stores, 'Store B', 'Updated description for Store B')
    print(get_stores_sorted_by_name(stores))