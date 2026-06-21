def validate_stores(stores):
    keywords = {'premium', 'organic', 'fresh'}
    for store in stores:
        if not keywords.issubset(store['description'].lower()):
            return False
    return True

if __name__ == '__main__':
    sample_stores = [
        {'name': 'Store A', 'description': 'Premium organic fresh produce'},
        {'name': 'Store B', 'description': 'Fresh and local products'},
        {'name': 'Store C', 'description': 'Organic and premium selections'}
    ]
    print(validate_stores(sample_stores))