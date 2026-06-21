def validate_stores(stores):
    keywords = {'premium', 'organic', 'fresh'}
    for store in stores:
        if not keywords.issubset(store['description'].lower()):
            return False
    return True

if __name__ == '__main__':
    sample_stores = [
        {'name': 'Green Grocer', 'description': 'Fresh produce and organic options'},
        {'name': 'Premium Market', 'description': 'Premium quality groceries'},
        {'name': 'Fresh Bazaar', 'description': 'Organic and fresh fruits and vegetables'}
    ]
    print(validate_stores(sample_stores))