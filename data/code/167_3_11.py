store_names = ["Bookshop", "Grocery Shop", "Electronics Store", "Bakery"]
store_ages = {name: 20 + i for i, name in enumerate(store_names)}

if __name__ == '__main__':
    print(store_ages)