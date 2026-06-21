class StoreAges:
    STORE_NAMES = {
        "Store A": 25,
        "Store B": 30,
        "Store C": 45,
        "Store D": 20,
        "Store E": 35
    }

    @staticmethod
    def display_store_ages(ages):
        for store, age in ages.items():
            print(f"{store}: {age} years old")

if __name__ == '__main__':
    StoreAges.display_store_ages(StoreAges.STORE_NAMES)