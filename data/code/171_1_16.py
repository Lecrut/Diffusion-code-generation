class StoreNameLength:
    def __init__(self):
        self.store_lengths = {}

    @staticmethod
    def normalize_name(name):
        return name.lower()

    def add_store(self, store_name):
        normalized_name = self.normalize_name(store_name)
        if normalized_name not in self.store_lengths:
            self.store_lengths[normalized_name] = len(store_name)

    def get_lengths(self):
        return self.store_lengths

if __name__ == '__main__':
    inventory = StoreNameLength()
    inventory.add_store("ABC Store")
    inventory.add_store("def store")
    inventory.add_store("GHIJ Store")
    print(inventory.get_lengths())