def last_element_generator(iterable):
    iterator = iter(iterable)
    try:
        while True:
            current = next(iterator)
            last = current
    except StopIteration:
        if 'last' in locals():
            yield last

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    generator = last_element_generator(sample_sequence)
    print(next(generator))