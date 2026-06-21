store_names = ["Bookstore", "Grocery Shop", "Electronics Store", "Bakery"]
store_ages = {name: age for name, age in zip(store_names, [25, 40, 33, 55])}

if __name__ == '__main__':
    print(store_ages)