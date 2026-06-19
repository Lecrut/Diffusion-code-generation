def last_element_generator(iterable):
    try:
        iterator = iter(iterable)
        while True:
            last = next(iterator)
    except StopIteration:
        yield last

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    generator = last_element_generator(sample_sequence)
    print(next(generator))