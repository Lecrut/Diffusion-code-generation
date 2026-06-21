def initialize_store_data():
    return [
        {"store_name": "Store A", "description": "A large retail location"},
        {"store_name": "Store B", "description": "Small boutique shop"},
        {"store_name": "Store C", "description": "Warehouse and distribution center"}
    ]

def update_store_description(stores, store_name, new_description):
    for store in stores:
        if store["store_name"] == store_name:
            store["description"] = new_description
            break

def get_stores_sorted_by_name(stores):
    return sorted(stores, key=lambda x: x["store_name"])

if __name__ == '__main__':
    stores = initialize_store_data()
    update_store_description(stores, "Store B", "Updated boutique shop")
    sorted_stores = get_stores_sorted_by_name(stores)
    print(sorted_stores)