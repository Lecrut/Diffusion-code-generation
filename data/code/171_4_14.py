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
        ("Apple", "Fruit"),
        ("Banana", "Fruit"),
        ("Carrot", "Vegetable"),
        ("Durian", "Exotic Fruit"),
        ("Eggplant", "Vegetable")
    ]
    print(group_stores_by_initial(sample_stores))