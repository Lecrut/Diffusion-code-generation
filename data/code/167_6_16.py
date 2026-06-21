class StoreManager:
    def __init__(self, store_names, ages):
        self.store_dict = dict(zip(store_names, ages))

    def get_store_ages(self):
        return self.store_dict

if __name__ == '__main__':
    store_names = ["Store A", "Store B", "Store C"]
    ages = [5, 3, 8]
    manager = StoreManager(store_names, ages)
    print(manager.get_store_ages())