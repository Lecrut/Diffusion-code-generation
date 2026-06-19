def second_element_generator(iterable):
    it = iter(iterable)
    try:
        first = next(it)
    except StopIteration:
        return
    try:
        yield next(it)
    except StopIteration:
        return

if __name__ == '__main__':
    sample_data_1 = [10, 20, 30, 40]
    sample_data_2 = [5, 15]
    sample_data_3 = [1]
    sample_data_4 = []

    gen1 = second_element_generator(sample_data_1)
    print(list(gen1))

    gen2 = second_element_generator(sample_data_2)
    print(list(gen2))

    gen3 = second_element_generator(sample_data_3)
    print(list(gen3))

    gen4 = second_element_generator(sample_data_4)
    print(list(gen4))