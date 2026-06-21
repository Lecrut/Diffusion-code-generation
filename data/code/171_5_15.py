def validate_batch_size(batch_size: int) -> None:
    if batch_size <= 0 or not isinstance(batch_size, int):
        raise ValueError('Batch size must be a positive integer')

def generate_store_batches(batch_size: int=50) -> iter:
    validate_batch_size(batch_size)
    store_names = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E']
    for i in range(0, len(store_names), batch_size):
        yield store_names[i:i + batch_size]
if __name__ == '__main__':
    batches = generate_store_batches()
    for batch in batches:
        print(batch)