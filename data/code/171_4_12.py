def group_stores_by_first_letter(stores):
    grouped = {}
    for name, description in stores:
        first_letter = name[0].upper()
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append((name, description))
    return grouped

if __name__ == '__main__':
    sample_stores = [
        ("Apple Store", "Sells apples and other fruits."),
        ("Banana Stand", "Freshly squeezed banana juice."),
        ("Cherry Orchard", "Grows and sells cherries."),
        ("Durian Market", "Exotic durian fruits for sale."),
        ("Elderberry Farm", "Organic elderberries.")
    ]
    result = group_stores_by_first_letter(sample_stores)
    print(result)