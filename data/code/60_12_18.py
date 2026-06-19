def last_element_generator(iterable):
    iterator = iter(iterable)
    try:
        while True:
            current = next(iterator)
    except StopIteration:
        yield None

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    generator = last_element_generator(sample_sequence)
    print(next(generator))