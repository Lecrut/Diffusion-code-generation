class StoreAges:
    STORE_AGE_MAP = {
        "Store A": 25,
        "Store B": 30,
        "Store C": 45,
        "Store D": 20,
        "Store E": 35
    }

    @staticmethod
    def display_store_ages():
        for store, age in StoreAges.STORE_AGE_MAP.items():
            print(f"{store}: {age} years old")

if __name__ == '__main__':
    StoreAges.display_store_ages()