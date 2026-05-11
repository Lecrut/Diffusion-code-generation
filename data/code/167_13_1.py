import random
data = {}
store_names = ["Bookstore", "Electronics", "Grocery", "Clothing", "Tools"]
ages = [25, 30, 45, 22, 50]
for i in range(len(store_names)):
    store_name = store_names[i]
    age = ages[i]
    if not isinstance(age, int) or age <= 0:
        print(f"Error: Invalid age provided for {store_name}. Age must be a positive integer.")
        continue
    data[store_name] = age
if __name__ == '__main__':
    print(data)