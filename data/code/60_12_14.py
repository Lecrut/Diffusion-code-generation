def last_element_generator(iterable):
    iterator = iter(iterable)
    try:
        while True:
            last = next(iterator)
    except StopIteration:
        if 'last' in locals():
            yield last

if __name__ == '__main__':
    sample_sequence = range(1000000)
    generator = last_element_generator(sample_sequence)
    print(next(generator))