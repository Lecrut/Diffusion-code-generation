store_names = ["Store A", "Store B", "Store C"]
ages = [5, 3, 8]

def create_store_dict(names, ages):
    if len(names) != len(ages):
        raise ValueError("Names and ages lists must have the same length")
    return dict(zip(names, ages))

if __name__ == '__main__':
    store_dict = create_store_dict(store_names, ages)
    print(store_dict)