def validate_batch_size(batch_size):
    if batch_size <= 0:
        raise ValueError('Batch size must be greater than zero')

def generate_store_names(start_index, end_index):
    store_names = [f'Store-{i}' for i in range(start_index, end_index + 1)]
    return store_names

def store_name_batch_generator(batch_size):
    validate_batch_size(batch_size)
    start_index = 0
    while True:
        batch = generate_store_names(start_index, start_index + batch_size - 1)
        if not batch:
            break
        yield batch
        start_index += batch_size
if __name__ == '__main__':
    batch_generator = store_name_batch_generator(50)
    for batch in range(3):
        print(next(batch_generator))