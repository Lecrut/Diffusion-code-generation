def first_element_generator(iterable):
    yield iterable[0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    generator = first_element_generator(sample_list)
    print(next(generator))