data = [
    {"store_name": "Store A", "description": "A large retail location"},
    {"store_name": "Store B", "description": "Small boutique shop"},
    {"store_name": "Store C", "description": "Warehouse and distribution center"}
]

def initialize_store_data():
    global data
    data = [
        {"store_name": "Store A", "description": "A large retail location"},
        {"store_name": "Store B", "description": "Small boutique shop"},
        {"store_name": "Store C", "description": "Warehouse and distribution center"}
    ]

def update_store_description(store_name, new_description):
    global data
    for store in data:
        if store["store_name"] == store_name:
            store["description"] = new_description
            return True
    return False

def get_stores_sorted():
    global data
    return sorted(data, key=lambda x: x["store_name"])

if __name__ == '__main__':
    initialize_store_data()
    update_store_description("Store B", "Modern grocery store")
    stores = get_stores_sorted()
    print(stores)