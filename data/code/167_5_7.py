stores_ages = {
    "StoreA": 30,
    "StoreB": 25,
    "StoreC": 40,
    "StoreD": 35,
    "StoreE": 28
}

if __name__ == '__main__':
    print("Stores and their ages:")
    for store, age in stores_ages.items():
        print(f"Store: {store}, Age: {age}")