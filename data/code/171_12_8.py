data = [
    {"store_name": "Store A", "description": "A large retail location"},
    {"store_name": "Store B", "description": "Small boutique shop"},
    {"store_name": "Store C", "description": "Warehouse and distribution center"}
]

def initialize_data():
    return data

def update_description(store_name, new_description):
    for store in data:
        if store["store_name"] == store_name:
            store["description"] = new_description
            break

def get_sorted_stores():
    return sorted(data, key=lambda x: x["store_name"])

if __name__ == '__main__':
    initialize_data()
    update_description("Store B", "Updated boutique shop")
    print(get_sorted_stores())