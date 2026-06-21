store_ages = {
    "Store A": 25,
    "Store B": 30,
    "Store C": 45,
    "Store D": 20,
    "Store E": 35
}

def display_store_ages(ages):
    for store, age in ages.items():
        print(f"{store}: {age} years old")

if __name__ == '__main__':
    sample_ages = {
        "Store F": 40,
        "Store G": 28,
        "Store H": 32
    }
    display_store_ages(sample_ages)