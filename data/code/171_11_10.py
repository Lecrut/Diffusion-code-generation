def filter_stores(stores):
    return {name: description for name, description in stores if description}

if __name__ == '__main__':
    store_data = [
        ("Store A", "A large retail location downtown."),
        ("Store B", ""),
        ("Store C", "A warehouse for electronics and gadgets.")
    ]
    filtered_stores = filter_stores(store_data)
    print(filtered_stores)