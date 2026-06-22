def positional_index_generator(iterable, index):
    for i, element in enumerate(iterable):
        if i == index:
            yield element

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_index = 2
    generator = positional_index_generator(sample_list, target_index)
    for value in generator:
        print(value)