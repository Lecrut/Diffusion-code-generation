class StoreData:
    def __init__(self):
        self.stores = {}
    def add_store(self, name, description):
        self.stores[name] = description
    def get_description(self, name):
        return self.stores.get(name)
if __name__ == '__main__':
    data_store = StoreData()
    data_store.add_store("Store A", "A large retail location downtown.")
    data_store.add_store("Store B", "A small boutique specializing in antiques.")
    data_store.add_store("Store C", "A warehouse for electronics and gadgets.")
    print(f"Description for Store A: {data_store.get_description('Store A')}")
    print(f"Description for Store B: {data_store.get_description('Store B')}")
    print(f"Description for Store C: {data_store.get_description('Store C')}")
    print(f"Description for Store D: {data_store.get_description('Store D')}")