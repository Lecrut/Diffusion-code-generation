def filter_and_map_stores(stores):
    filtered_stores = {name: description for name, description in stores if description}
    return filtered_stores
if __name__ == '__main__':
    sample_stores = [('Store A', 'A large retail location downtown.'), ('Store B', ''), ('Store C', 'A warehouse for electronics and gadgets.')]
    filtered_stores = filter_and_map_stores(sample_stores)
    print(filtered_stores)