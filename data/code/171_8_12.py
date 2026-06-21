def validate_stores(stores):
    keywords = {'premium', 'organic', 'fresh'}
    for store in stores:
        if not any(keyword in store.lower() for keyword in keywords):
            return False
    return True

if __name__ == '__main__':
    sample_stores = [
        "Fresh Market",
        "Organic Oasis",
        "Premium Produce",
        "Healthy Haven"
    ]
    print(validate_stores(sample_stores))