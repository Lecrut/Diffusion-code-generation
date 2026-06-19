def last_element_generator(iterable):
    last = None
    for item in iterable:
        last = item
    if last is not None:
        yield last

if __name__ == '__main__':
    sample_sequence = range(1000000)
    generator = last_element_generator(sample_sequence)
    print(next(generator))