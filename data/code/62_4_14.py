def second_element_generator(iterable):
    iterator = iter(iterable)
    try:
        first_element = next(iterator)
        second_element = next(iterator)
        yield second_element
    except StopIteration:
        return

if __name__ == '__main__':
    sample_data_1 = [1, 2, 3, 4]
    gen1 = second_element_generator(sample_data_1)
    print(list(gen1))

    sample_data_2 = ['a', 'b']
    gen2 = second_element_generator(sample_data_2)
    print(list(gen2))

    sample_data_3 = [100]
    gen3 = second_element_generator(sample_data_3)
    print(list(gen3))

    sample_data_4 = []
    gen4 = second_element_generator(sample_data_4)
    print(list(gen4))