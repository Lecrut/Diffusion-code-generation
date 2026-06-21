class StoreAgeMapper:
    STORE_NAMES = ["Bookstore", "Grocery Shop", "Electronics Store", "Bakery"]
    DEFAULT_AGE = 30

    @staticmethod
    def map_store_ages():
        return {name: age for name, age in zip(StoreAgeMapper.STORE_NAMES, [25, 40, 33, 55])}

if __name__ == '__main__':
    store_ages = StoreAgeMapper.map_store_ages()
    print(store_ages)