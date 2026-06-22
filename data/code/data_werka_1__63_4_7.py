def first_element_generator(iterable):
    return (item for item in iterable)

if __name__ == '__main__':
    sample_iterable = [10, 20, 30, 40, 50]
    generator = first_element_generator(sample_iterable)
    print(next(generator))