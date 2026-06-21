def initialize_stores():
    return [
        {'name': 'Store A', 'description': 'Electronics'},
        {'name': 'Store B', 'description': 'Clothing'},
        {'name': 'Store C', 'description': 'Books'}
    ]

def update_store_description(stores, name, description):
    for store in stores:
        if store['name'] == name:
            store['description'] = description
            break

def get_stores_sorted_by_name(stores):
    return sorted(stores, key=lambda x: x['name'])

if __name__ == '__main__':
    stores = initialize_stores()
    update_store_description(stores, 'Store B', 'Home Appliances')
    print(get_stores_sorted_by_name(stores))