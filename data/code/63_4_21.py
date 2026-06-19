def first_element_generator(iterable):
    iterator = iter(iterable)
    try:
        first_item = next(iterator)
        yield first_item
    except StopIteration:
        raise ValueError("The iterable is empty")

if __name__ == '__main__':
    sample_iterable = [3, 6, 9, 12, 15]
    generator = first_element_generator(sample_iterable)
    print(next(generator))