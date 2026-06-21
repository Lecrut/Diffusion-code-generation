STORE_AGE_MAP = {
    "Store Alpha": 25,
    "Store Beta": 30,
    "Store Gamma": 35
}

def validate_store_name(store_name):
    if store_name not in STORE_AGE_MAP:
        raise ValueError(f"Invalid store name: {store_name}")
    return True

def get_store_age(store_name):
    validate_store_name(store_name)
    return STORE_AGE_MAP[store_name]

if __name__ == '__main__':
    sample_store = "Store Beta"
    print(f"The age of {sample_store} is {get_store_age(sample_store)}")