STORE_AGE_THRESHOLD = 30

store_ages = {
    "Store A": 25,
    "Store B": 30,
    "Store C": 45,
    "Store D": 20,
    "Store E": 35
}

def is_store_age_valid(age):
    return isinstance(age, int) and age >= STORE_AGE_THRESHOLD

if __name__ == '__main__':
    valid_ages = {store: age for store, age in store_ages.items() if is_store_age_valid(age)}
    print(valid_ages)