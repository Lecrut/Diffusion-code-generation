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
        ("Apple Store", "A place to buy Apple products."),
        ("Best Buy", "Electronics and home appliances."),
        ("Barnes & Noble", "Books and educational materials."),
        ("Circuit City", "Electronics and computer accessories."),
        ("Dell", "Computers and peripherals.")
    ]
    grouped_stores = group_stores_by_first_letter(sample_stores)
    print(grouped_stores)