def first_element_generator(iterable):
    iterator = iter(iterable)
    try:
        yield next(iterator)
    except StopIteration:
        raise ValueError("The iterable is empty")

if __name__ == '__main__':
    sample_iterable = [10, 20, 30, 40, 50]
    generator = first_element_generator(sample_iterable)
    print(next(generator))