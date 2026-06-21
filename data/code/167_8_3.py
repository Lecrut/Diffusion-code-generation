store_ages = {
    "Store X": 25,
    "Store Y": 30,
    "Store Z": 35
}

def get_store_age(store_name):
    return store_ages.get(store_name, None)

if __name__ == '__main__':
    sample_store = "Store Y"
    print(f"The age of {sample_store} is {get_store_age(sample_store)}")