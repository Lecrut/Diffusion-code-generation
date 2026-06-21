def generate_ages(stores):
    return [len(store) for store in stores]

def zip_stores_and_ages(stores):
    ages = generate_ages(stores)
    return dict(zip(stores, ages))

if __name__ == '__main__':
    sample_stores = ["StoreA", "StoreB", "StoreC"]
    result = zip_stores_and_ages(sample_stores)
    print(result)