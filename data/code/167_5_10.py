stores = {
    "StoreA": 30,
    "StoreB": 25,
    "StoreC": 35,
    "StoreD": 40,
    "StoreE": 22
}

if __name__ == '__main__':
    for store_name, age in stores.items():
        print(f"Store: {store_name}, Age: {age}")