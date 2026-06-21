STORE_AGE_MAP = {
    "Store A": 25,
    "Store B": 30,
    "Store C": 35
}

def validate_store_name(store_name):
    if store_name not in STORE_AGE_MAP:
        raise ValueError(f"Invalid store name: {store_name}")

def get_store_age(store_name):
    validate_store_name(store_name)
    return STORE_AGE_MAP[store_name]

if __name__ == '__main__':
    sample_store = "Store B"
    print(f"The age of {sample_store} is {get_store_age(sample_store)}")