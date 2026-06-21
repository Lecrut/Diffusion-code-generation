STORE_NAMES = ["Bookstore", "Grocery Shop", "Electronics Store", "Bakery"]
AGE_MAP = {name: age for name, age in zip(STORE_NAMES, [25, 40, 33, 55])}

if __name__ == '__main__':
    print(AGE_MAP)