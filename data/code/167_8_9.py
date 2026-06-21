store_ages = {
    "Store Alpha": 25,
    "Store Beta": 30,
    "Store Gamma": 35
}

def get_store_age(store_name):
    return store_ages.get(store_name, None)

if __name__ == '__main__':
    sample_store = "Store Beta"
    age = get_store_age(sample_store)
    print(f"The age of {sample_store} is {age}")