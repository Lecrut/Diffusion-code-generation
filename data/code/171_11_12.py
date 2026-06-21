class StoreData:
    def __init__(self):
        self.stores = {}

    def add_store(self, name, description):
        if description:
            self.stores[name] = description

    def get_descriptions(self):
        return self.stores

if __name__ == '__main__':
    data_store = StoreData()
    data_store.add_store("Store A", "A large retail location downtown.")
    data_store.add_store("Store B", "")
    data_store.add_store("Store C", "A warehouse for electronics and gadgets.")

    descriptions = data_store.get_descriptions()

    print(f"Description for Store A: {descriptions.get('Store A')}")
    print(f"Description for Store B: {descriptions.get('Store B')}")
    print(f"Description for Store C: {descriptions.get('Store C')}")