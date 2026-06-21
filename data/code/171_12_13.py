stores = [
    {"store_name": "Store A", "description": "A large retail location"},
    {"store_name": "Store B", "description": "Small boutique shop"},
    {"store_name": "Store C", "description": "Warehouse and distribution center"}
]

def initialize_data():
    global stores
    stores = [
        {"store_name": "Store A", "description": "A large retail location"},
        {"store_name": "Store B", "description": "Small boutique shop"},
        {"store_name": "Store C", "description": "Warehouse and distribution center"}
    ]

def update_description(store_name, new_description):
    global stores
    for store in stores:
        if store["store_name"] == store_name:
            store["description"] = new_description

def get_sorted_stores():
    return sorted(stores, key=lambda x: x["store_name"])

if __name__ == '__main__':
    initialize_data()
    update_description("Store B", "Updated small boutique shop")
    print(get_sorted_stores())