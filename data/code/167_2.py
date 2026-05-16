class StoreInventory:
    def __init__(self, store_names, ages):
        self.store_names = store_names
        self.ages = ages
    def display_data(self):
        for name, age in zip(self.store_names, self.ages):
            print(f"Store: {name}, Age: {age}")
if __name__ == '__main__':
    store_names_list = ["Store A", "Store B", "Store C"]
    ages_list = [25, 30, 22]
    inventory = StoreInventory(store_names_list, ages_list)
    inventory.display_data()