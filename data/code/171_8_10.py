def validate_stores(stores):
    keywords = {'premium', 'organic', 'fresh'}
    for store in stores:
        if not keywords.issubset(store['description'].lower()):
            return False
    return True

if __name__ == '__main__':
    sample_stores = [
        {'name': 'Green Grocer', 'description': 'Fresh produce, organic options'},
        {'name': 'Premium Market', 'description': 'Premium quality products'},
        {'name': 'Fresh Bazaar', 'description': 'Organic and fresh selections'}
    ]
    print(validate_stores(sample_stores))