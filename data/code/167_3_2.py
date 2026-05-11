import random
store_data = {}
store_names = ["Bookstore", "Grocery", "Electronics", "Clothing"]
ages = [25, 30, 45, 22]
for name, age in zip(store_names, ages):
    try:
        store_data[name] = age
    except ValueError:
        print(f"Error: Invalid age input for store {name}")
if __name__ == '__main__':
    pass