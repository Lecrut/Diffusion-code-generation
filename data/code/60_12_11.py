def last_element_generator(iterable):
    try:
        iterator = iter(iterable)
        last = next(iterator)
        for item in iterator:
            last = item
        yield last
    except TypeError:
        raise ValueError('Input must be an iterable')
if __name__ == '__main__':
    sample_sequence = (x for x in range(1000000))
    try:
        generator = last_element_generator(sample_sequence)
        print(next(generator))
    except ValueError as e:
        print(e)