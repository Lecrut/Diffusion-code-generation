def positional_index_generator(iterable, index):
    for i, element in enumerate(iterable):
        if i == index:
            yield element

if __name__ == '__main__':
    sample_sequence = range(1000000)
    target_index = 500000
    generator = positional_index_generator(sample_sequence, target_index)
    for value in generator:
        print(value)