def filter_stores(stores):
    return {name: desc for name, desc in stores if desc}

if __name__ == '__main__':
    sample_stores = [
        ("Store A", "A large retail location downtown."),
        ("Store B", ""),
        ("Store C", "A warehouse for electronics and gadgets.")
    ]
    filtered_stores = filter_stores(sample_stores)
    print(filtered_stores)