def first_element_generator(iterable):
    yield next(iterable)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    generator = first_element_generator(iter(sample_list))
    print(next(generator))