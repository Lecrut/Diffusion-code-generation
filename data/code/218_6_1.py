def find_minimum_generator(data):
    if not data:
        return
    current_min = data[0]
    yield current_min
    for element in data[1:]:
        if element < current_min:
            current_min = element
            yield current_min
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3]
    minimum_generator = find_minimum_generator(sample_list)
    result = list(minimum_generator)
    print(result)
    sample_list_2 = [42, 10, 55, 33]
    minimum_generator_2 = find_minimum_generator(sample_list_2)
    result_2 = list(minimum_generator_2)
    print(result_2)
    sample_list_3 = [7]
    minimum_generator_3 = find_minimum_generator(sample_list_3)
    result_3 = list(minimum_generator_3)
    print(result_3)
    sample_list_4 = []
    minimum_generator_4 = find_minimum_generator(sample_list_4)
    result_4 = list(minimum_generator_4)
    print(result_4)