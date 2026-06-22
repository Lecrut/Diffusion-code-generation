def first_element_generator(iterable):
    iterator = iter(iterable)
    try:
        yield next(iterator)
    except StopIteration:
        raise ValueError("The iterable is empty")

if __name__ == '__main__':
    sample_iterable = [5, 10, 15, 20, 25]
    generator = first_element_generator(sample_iterable)
    print(next(generator))