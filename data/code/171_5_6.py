def store_name_generator():
    stores = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E', 'Store 496', 'Store 497', 'Store 498', 'Store 499', 'Store 500']
    for i in range(0, len(stores), 50):
        yield stores[i:i + 50]
if __name__ == '__main__':
    gen = store_name_generator()
    batch = next(gen)
    print(batch)