def group_stores_by_name(stores):
    groups = {}
    for name, description in stores:
        first_letter = name[0].upper()
        if first_letter not in groups:
            groups[first_letter] = []
        groups[first_letter].append((name, description))
    return groups

if __name__ == '__main__':
    sample_stores = [
        ("Apple", "A fruit"),
        ("Banana", "A yellow fruit"),
        ("Cherry", "A small red fruit"),
        ("Date", "A sweet fruit"),
        ("Elderberry", "A purple berry")
    ]
    grouped_stores = group_stores_by_name(sample_stores)
    print(grouped_stores)