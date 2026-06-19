def first_element_generator(iterable):
    yield next(iterable)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    generator = first_element_generator(iter(sample_list))
    print(next(generator))