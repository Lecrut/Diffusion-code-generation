stores = {
    "StoreA": 30,
    "StoreB": 25,
    "StoreC": 40,
    "StoreD": 22,
    "StoreE": 35
}

if __name__ == '__main__':
    print("Stores and their ages:")
    for store_name, age in stores.items():
        print(f"Store: {store_name}, Age: {age}")