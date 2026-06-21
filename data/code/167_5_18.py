class StoreData:
    STORE_AGE = 30
    STORE_B_AGE = 25
    STORE_C_AGE = 35
    STORE_D_AGE = 40
    STORE_E_AGE = 22

    @staticmethod
    def get_store_ages():
        return {
            "StoreA": StoreData.STORE_AGE,
            "StoreB": StoreData.STORE_B_AGE,
            "StoreC": StoreData.STORE_C_AGE,
            "StoreD": StoreData.STORE_D_AGE,
            "StoreE": StoreData.STORE_E_AGE
        }

if __name__ == '__main__':
    store_ages = StoreData.get_store_ages()
    print("Store Ages:")
    for store, age in store_ages.items():
        print(f"Store: {store}, Age: {age}")