def first_element_generator(iterable):
    iterator = iter(iterable)
    try:
        yield next(iterator)
    except StopIteration:
        raise ValueError("The iterable is empty")

if __name__ == '__main__':
    SAMPLE_ITERABLE = [9, 18, 27, 36, 45]
    generator = first_element_generator(SAMPLE_ITERABLE)
    print(next(generator))