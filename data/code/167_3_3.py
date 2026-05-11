import random
store_data = {}
store_names = ["Bookstore", "Electronics Shop", "Grocery Mart", "Clothing Boutique"]
ages = [25, 30, 45, 22]
for name, age in zip(store_names, ages):
    try:
        store_data[name] = int(age)
    except ValueError:
        print(f"Error: Invalid age input for store {name}. Skipping.")
if __name__ == '__main__':
    pass