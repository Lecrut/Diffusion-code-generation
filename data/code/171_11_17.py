def filter_stores(stores):
    return {name: description for name, description in stores if description}

def main():
    sample_stores = [('Store A', 'A large retail location downtown.'), ('Store B', ''), ('Store C', 'A warehouse for electronics and gadgets.'), ('Store D', None)]
    filtered_stores = filter_stores(sample_stores)
    print(filtered_stores)
if __name__ == '__main__':
    main()