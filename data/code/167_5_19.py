if __name__ == '__main__':
    STORE_AGE_DATA = {
        "StoreA": 30,
        "StoreB": 25,
        "StoreC": 35,
        "StoreD": 40,
        "StoreE": 22
    }
    for store, age in STORE_AGE_DATA.items():
        print(f"Store: {store}, Age: {age}")