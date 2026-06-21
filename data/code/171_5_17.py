def store_name_generator():
    store_names = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E']
    for i in range(0, len(store_names), 50):
        yield store_names[i:i + 50]
if __name__ == '__main__':
    gen = store_name_generator()
    batch1 = next(gen)
    print(batch1)