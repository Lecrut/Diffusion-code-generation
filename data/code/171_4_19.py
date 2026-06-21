def group_stores_by_initial(stores):
    grouped = {}
    for name, description in stores:
        initial = name[0].upper()
        if initial not in grouped:
            grouped[initial] = []
        grouped[initial].append((name, description))
    return grouped

if __name__ == '__main__':
    sample_stores = [
        ("Apple Store", "Sells apples and other fruits."),
        ("Banana Stand", "Freshly squeezed banana juice."),
        ("Cherry Bakery", "Sweet cherries and cherry products."),
        ("Durian Market", "Exotic durians for sale.")
    ]
    result = group_stores_by_initial(sample_stores)
    print(result)