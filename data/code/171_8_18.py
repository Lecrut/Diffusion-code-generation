def validate_stores(stores):
    keywords = {'premium', 'organic', 'fresh'}
    for store in stores:
        if not keywords.issubset(store['description'].lower()):
            return False
    return True

if __name__ == '__main__':
    sample_stores = [
        {'name': 'Store A', 'description': 'Premium Organic Fresh Produce'},
        {'name': 'Store B', 'description': 'Organic Fresh Produce'},
        {'name': 'Store C', 'description': 'Fresh Produce'}
    ]
    print(validate_stores(sample_stores))