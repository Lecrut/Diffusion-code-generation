def validate_stores(stores):
    keywords = {'premium', 'organic', 'fresh'}
    for store in stores:
        if not any(keyword in store for keyword in keywords):
            return False
    return True

if __name__ == '__main__':
    sample_stores = [
        "Premium Fresh Organic Groceries",
        "Healthy Organic Foods",
        "Fresh Produce Market"
    ]
    print(validate_stores(sample_stores))