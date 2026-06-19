def second_element_generator(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
        return next(iterator)
    except StopIteration:
        return None

if __name__ == '__main__':
    sample_data1 = [10, 20, 30, 40]
    print(second_element_generator(sample_data1))
    sample_data2 = [5, 15]
    print(second_element_generator(sample_data2))
    sample_data3 = [1]
    print(second_element_generator(sample_data3))
    sample_data4 = []
    print(second_element_generator(sample_data4))