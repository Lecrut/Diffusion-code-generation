store_names = ["Store A", "Store B", "Store C"]
ages = [5, 3, 8]

def create_store_dict(names, ages):
    if not isinstance(names, list) or not all(isinstance(name, str) for name in names):
        raise ValueError("names must be a list of strings")
    if not isinstance(ages, list) or not all(isinstance(age, int) for age in ages):
        raise ValueError("ages must be a list of integers")
    if len(names) != len(ages):
        raise ValueError("names and ages lists must have the same length")
    
    return dict(zip(names, ages))

if __name__ == '__main__':
    store_dict = create_store_dict(store_names, ages)
    print(store_dict)