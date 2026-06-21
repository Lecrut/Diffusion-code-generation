stores = [
    {'name': 'Store A', 'description': 'Description for Store A'},
    {'name': 'Store B', 'description': 'Description for Store B'},
    {'name': 'Store C', 'description': 'Description for Store C'}
]

def update_store_description(name, new_description):
    global stores
    for store in stores:
        if store['name'] == name:
            store['description'] = new_description
            break

def get_stores_sorted_by_name():
    return sorted(stores, key=lambda x: x['name'])

if __name__ == '__main__':
    update_store_description('Store B', 'Updated description for Store B')
    print(get_stores_sorted_by_name())