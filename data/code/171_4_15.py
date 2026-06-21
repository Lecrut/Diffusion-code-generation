def group_stores_by_name(stores):
    grouped = {}
    for name, description in stores:
        first_letter = name[0].upper()
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append((name, description))
    return grouped

if __name__ == '__main__':
    stores = [
        ("Apple Store", "A place to buy Apple products."),
        ("Best Buy", "Electronics and home appliances store."),
        ("Costco", "Warehouse club with groceries and electronics."),
        ("Dell", "Computer store specializing in Dell products."),
        ("Epicurious", "Cooking classes and recipes.")
    ]
    result = group_stores_by_name(stores)
    print(result)