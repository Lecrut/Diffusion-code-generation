STORE_AGE_MAP = {
    "Store A": 25,
    "Store B": 30,
    "Store C": 35
}

def get_store_age(store_name):
    return STORE_AGE_MAP.get(store_name, None)

if __name__ == '__main__':
    sample_store = "Store B"
    print(f"The age of {sample_store} is {get_store_age(sample_store)}")