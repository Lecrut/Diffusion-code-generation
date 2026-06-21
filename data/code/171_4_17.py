def group_stores_by_initial(stores):
    if not stores:
        return {}
    
    grouped_stores = {}
    for name, description in stores:
        initial = name[0].upper()
        if initial not in grouped_stores:
            grouped_stores[initial] = []
        grouped_stores[initial].append((name, description))
    
    return grouped_stores

if __name__ == '__main__':
    sample_stores = [
        ("Apple Store", "A place to buy apples and electronics."),
        ("Banana Mart", "Selling bananas and related products."),
        ("Cherry Corner", "Fresh cherries and other fruits."),
        ("Doughnut Depot", "Donuts in various flavors.")
    ]
    
    result = group_stores_by_initial(sample_stores)
    print(result)