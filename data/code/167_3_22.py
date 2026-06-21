store_names = ["Bookstore", "Grocery Shop", "Electronics Store", "Bakery"]
expected_ages = [25, 40, 33, 55]

def validate_input(names, ages):
    if len(names) != len(ages):
        raise ValueError("The number of store names and ages must be the same.")
    for age in ages:
        if not isinstance(age, int) or age <= 0:
            raise ValueError("All ages must be positive integers.")

def map_store_ages(names, ages):
    validate_input(names, ages)
    return {name: age for name, age in zip(names, ages)}

if __name__ == '__main__':
    store_ages = map_store_ages(store_names, expected_ages)
    print(store_ages)