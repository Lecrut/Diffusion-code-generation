def validate_store_ages(ages):
    if not all(isinstance(age, int) for age in ages.values()):
        raise ValueError("All store ages must be integers.")
    if any(age < 0 for age in ages.values()):
        raise ValueError("Age cannot be negative.")

if __name__ == '__main__':
    stores = {
        "StoreA": 30,
        "StoreB": 25,
        "StoreC": 35,
        "StoreD": 40,
        "StoreE": 22
    }
    
    validate_store_ages(stores)
    
    for store, age in stores.items():
        print(f"Store: {store}, Age: {age}")