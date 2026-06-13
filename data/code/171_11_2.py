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
    print(f"Description for Store A: {data_structure.get_description('Store A')}")
    print(f"Description for Store B: {data_structure.get_description('Store B')}")
    print(f"Description for Store C: {data_structure.get_description('Store C')}")
    print(f"Description for Store D: {data_structure.get_description('Store D')}")