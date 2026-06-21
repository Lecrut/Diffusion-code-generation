def validate_store_names(store_names):
    if not all(isinstance(name, str) for name in store_names):
        raise ValueError("All store names must be strings.")
    return store_names

def validate_ages(ages):
    if not all(isinstance(age, int) and age >= 0 for age in ages):
        raise ValueError("All ages must be non-negative integers.")
    return ages

def map_store_ages(store_names, ages):
    store_names = validate_store_names(store_names)
    ages = validate_ages(ages)
    return {name: age for name, age in zip(store_names, ages)}

if __name__ == '__main__':
    store_names = ["Bookstore", "Grocery Shop", "Electronics Store", "Bakery"]
    ages = [25, 40, 33, 55]
    store_ages = map_store_ages(store_names, ages)
    print(store_ages)