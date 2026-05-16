import random
store_data = {}
store_names = ["Bookstore", "Grocery Shop", "Electronics Store", "Bakery"]
ages = [25, 40, 33, 55]
for name, age in zip(store_names, ages):
    try:
        store_data[name] = int(age)
    except ValueError:
        print(f"Error: Invalid age input for store {name}. Skipping.")
if __name__ == '__main__':
    print(store_data)