def store_name_generator(store_list):
    batch_size = 50
    for i in range(0, len(store_list), batch_size):
        yield store_list[i:i + batch_size]
if __name__ == '__main__':
    large_store_dataset = ['Store1', 'Store2', 'Store3', ..., 'Store1500']
    generator = store_name_generator(large_store_dataset)
    for batch in generator:
        print(batch)