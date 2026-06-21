store_names = ["Store A", "Store B", "Store C"]
ages = [5, 3, 8]

def zip_stores_and_ages(names, ages):
    return dict(zip(names, ages))

if __name__ == '__main__':
    store_dict = zip_stores_and_ages(store_names, ages)
    print(store_dict)