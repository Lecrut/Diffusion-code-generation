def first_element_generator(iterable):
    iterator = iter(iterable)
    try:
        yield next(iterator)
    except StopIteration:
        raise ValueError("The iterable is empty")

if __name__ == '__main__':
    sample_iterable_1 = [5, 10, 15, 20, 25]
    generator_1 = first_element_generator(sample_iterable_1)
    print(next(generator_1))

    sample_iterable_2 = ['a', 'b', 'c']
    generator_2 = first_element_generator(sample_iterable_2)
    print(next(generator_2))

    empty_iterable = []
    try:
        generator_empty = first_element_generator(empty_iterable)
        print(next(generator_empty))
    except ValueError as e:
        print(e)