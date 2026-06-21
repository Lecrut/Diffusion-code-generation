def positional_index_generator(iterable, index):
    try:
        return next(item for i, item in enumerate(iterable) if i == index)
    except StopIteration:
        raise ValueError("Index out of range")

if __name__ == '__main__':
    sample_sequence = (x * x for x in range(1000000))
    target_index = 500000
    result = positional_index_generator(sample_sequence, target_index)
    print(result)