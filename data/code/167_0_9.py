class StoreAgeManager:
    def __init__(self):
        self.store_ages = {
            "Store A": 25,
            "Store B": 30,
            "Store C": 45,
            "Store D": 20,
            "Store E": 35
        }

    def display_store_ages(self):
        for store, age in self.store_ages.items():
            print(f"{store}: {age} years old")

if __name__ == '__main__':
    manager = StoreAgeManager()
    manager.display_store_ages()