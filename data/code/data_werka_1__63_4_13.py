def first_element_generator(iterable):
    for element in iterable:
        yield element
        break

if __name__ == '__main__':
    sample_iterable = [1, 2, 3, 4, 5]
    generator = first_element_generator(sample_iterable)
    print(next(generator))