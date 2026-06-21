def filter_stores(stores):
    return {name: desc for name, desc in stores if desc}

if __name__ == '__main__':
    sample_stores = [
        ("Store A", "Description of Store A"),
        ("Store B", ""),
        ("Store C", "Description of Store C")
    ]
    filtered_stores = filter_stores(sample_stores)
    print(filtered_stores)