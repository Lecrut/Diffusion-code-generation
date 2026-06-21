store_ages = {
    "Store Alpha": 25,
    "Store Beta": 30,
    "Store Gamma": 45,
    "Store Delta": 20,
    "Store Echo": 35
}

def update_store_age(store_name, age):
    if not isinstance(store_name, str) or store_name.strip() == "":
        raise ValueError("Invalid store name")
    if not isinstance(age, int) or age < 0:
        raise ValueError("Invalid age")
    store_ages[store_name] = age

def remove_store_age(store_name):
    validate_store_name(store_name)
    store_ages.pop(store_name, None)

def list_all_stores():
    for store, age in store_ages.items():
        print(f"{store}: {age} years old")

if __name__ == '__main__':
    update_store_age("Store Beta", 32)
    remove_store_age("Store Gamma")
    list_all_stores()