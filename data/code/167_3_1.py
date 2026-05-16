store_data = {}
store_names = ["StoreA", "StoreB", "StoreC"]
ages = [25, 30, "thirty"]
if len(store_names) != len(ages):
    exit()
for name, age in zip(store_names, ages):
    try:
        age_int = int(age)
        store_data[name] = age_int
    except ValueError:
        print(f"Error: Invalid age input for {name}. Skipping entry.")
if __name__ == '__main__':
    pass