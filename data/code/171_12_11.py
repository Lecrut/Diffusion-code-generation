stores = [
    {'name': 'Store A', 'description': 'Description for Store A'},
    {'name': 'Store B', 'description': 'Description for Store B'},
    {'name': 'Store C', 'description': 'Description for Store C'}
]

def initialize_data():
    global stores
    stores = [
        {'name': 'Store A', 'description': 'Description for Store A'},
        {'name': 'Store B', 'description': 'Description for Store B'},
        {'name': 'Store C', 'description': 'Description for Store C'}
    ]

def update_description(name, description):
    global stores
    for store in stores:
        if store['name'] == name:
            store['description'] = description

def get_all_stores_sorted():
    return sorted(stores, key=lambda x: x['name'])

if __name__ == '__main__':
    initialize_data()
    update_description('Store B', 'Updated description for Store B')
    print(get_all_stores_sorted())