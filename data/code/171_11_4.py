class StoreData:
    def __init__(self):
        self.stores = {}
    def add_store(self, name, description):
        self.stores[name] = description
    def get_description(self, name):
        return self.stores.get(name)
if __name__ == '__main__':
    data_structure = StoreData()
    data_structure.add_store("Store A", "A large retail location downtown.")
    data_structure.add_store("Store B", "A small boutique specializing in antiques.")
    data_structure.add_store("Store C", "A large warehouse for electronics.")
    print("--- Store Data Lookup ---")
    store_name_to_find = "Store B"
    description = data_structure.get_description(store_name_to_find)
    if description is not None:
        print(f"Description for {store_name_to_find}: {description}")
    else:
        print(f"Store {store_name_to_find} not found.")
    store_name_to_find = "Store A"
    description = data_structure.get_description(store_name_to_find)
    if description is not None:
        print(f"Description for {store_name_to_find}: {description}")
    else:
        print(f"Store {store_name_to_find} not found.")