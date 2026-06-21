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
        ("Apple Store", "Sells various Apple products."),
        ("Best Buy", "Electronics and home appliances."),
        ("Circuit City", "Electronics and computer accessories."),
        ("Dell", "Computers and peripherals."),
        ("Epicenter", "Mobile phones and accessories.")
    ]
    result = group_stores_by_first_letter(sample_stores)
    print(result)