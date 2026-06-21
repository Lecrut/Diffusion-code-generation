def group_stores_by_initial(stores):
    grouped = {}
    for name, description in stores:
        initial = name[0].upper()
        if initial not in grouped:
            grouped[initial] = []
        grouped[initial].append((name, description))
    return grouped

if __name__ == '__main__':
    stores = [
        ("Apple", "A fruit"),
        ("Banana", "A yellow fruit"),
        ("Cherry", "A small red fruit"),
        ("Date", "A sweet fruit"),
        ("Elderberry", "A purple berry")
    ]
    grouped_stores = group_stores_by_initial(stores)
    print(grouped_stores)