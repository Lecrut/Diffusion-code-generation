store_ages = {
    "Store Alpha": 25,
    "Store Beta": 30,
    "Store Gamma": 35
}

def get_store_age(store_name):
    if store_name not in store_ages:
        raise ValueError(f"Invalid store name: {store_name}")
    return store_ages[store_name]

if __name__ == '__main__':
    sample_store = "Store Beta"
    try:
        print(f"The age of {sample_store} is {get_store_age(sample_store)}")
    except ValueError as e:
        print(e)