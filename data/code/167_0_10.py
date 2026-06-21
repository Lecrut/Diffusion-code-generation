store_ages = {
    "Store A": 25,
    "Store B": 30,
    "Store C": 45,
    "Store D": 20,
    "Store E": 35
}

def validate_store_name(store_name):
    if not isinstance(store_name, str) or store_name.strip() == "":
        raise ValueError("Invalid store name")

def get_store_age(store_name):
    validate_store_name(store_name)
    return store_ages.get(store_name, None)

if __name__ == '__main__':
    print(get_store_age("Store B"))