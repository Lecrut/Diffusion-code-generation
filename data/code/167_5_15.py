store_ages = {
    "StoreA": 30,
    "StoreB": 25,
    "StoreC": 40,
    "StoreD": 35,
    "StoreE": 28
}

if __name__ == '__main__':
    for store_name, age in store_ages.items():
        print(f"Store: {store_name}, Age: {age}")