store_names = ["Bookstore", "Grocery Shop", "Electronics Store", "Bakery"]
expected_ages = [25, 40, 33, 55]

def validate_input(names, ages):
    if len(names) != len(ages):
        raise ValueError("Mismatch between number of store names and ages")
    for age in ages:
        if not isinstance(age, int):
            raise ValueError(f"Invalid age input: {age}")

def map_store_ages(names, ages):
    validate_input(names, ages)
    return {name: age for name, age in zip(names, ages)}

if __name__ == '__main__':
    store_ages = map_store_ages(store_names, expected_ages)
    print(store_ages)