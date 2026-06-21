class StoreData:
    STORE_AGE = {
        "StoreA": 30,
        "StoreB": 25,
        "StoreC": 35,
        "StoreD": 40,
        "StoreE": 22
    }

    @staticmethod
    def get_store_ages():
        return StoreData.STORE_AGE

if __name__ == '__main__':
    store_ages = StoreData.get_store_ages()
    print("Store ages:")
    for store, age in store_ages.items():
        print(f"{store}: {age}")