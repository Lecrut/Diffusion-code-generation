def batch_store_names(batch_size=50):
    store_names = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E', 'Store Z']
    for i in range(0, len(store_names), batch_size):
        yield store_names[i:i + batch_size]
if __name__ == '__main__':
    for batch in batch_store_names():
        print(batch)