def first_element_generator(iterable):
    try:
        yield iterable[0]
    except IndexError:
        raise ValueError("The iterable is empty")

if __name__ == '__main__':
    sample_iterable = [1, 2, 3, 4, 5]
    generator = first_element_generator(sample_iterable)
    print(next(generator))