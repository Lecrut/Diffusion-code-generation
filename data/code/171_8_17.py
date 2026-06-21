def validate_stores(stores):
    keywords = {'premium', 'organic', 'fresh'}
    for store in stores:
        if not keywords.issubset(store.lower()):
            return False
    return True

if __name__ == '__main__':
    sample_stores = [
        "Premium Fresh Market",
        "Organic Grocer",
        "Fresh Produce Store"
    ]
    print(validate_stores(sample_stores))