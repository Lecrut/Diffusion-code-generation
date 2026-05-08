def largest_element_generator(data):
    if not data:
        return
    current_max = data[0]
    yield current_max
    for element in data[1:]:
        if element > current_max:
            current_max = element
        yield current_max
if __name__ == '__main__':
    sample_list = [3, 15, 7, 42, 8, 29]
    generator = largest_element_generator(sample_list)
    result = list(generator)
    print(result)
    sample_list_2 = [100, 5, 200, 1, 150]
    generator_2 = largest_element_generator(sample_list_2)
    result_2 = list(generator_2)
    print(result_2)
    sample_list_3 = [5]
    generator_3 = largest_element_generator(sample_list_3)
    result_3 = list(generator_3)
    print(result_3)
    sample_list_4 = []
    generator_4 = largest_element_generator(sample_list_4)
    result_4 = list(generator_4)
    print(result_4)