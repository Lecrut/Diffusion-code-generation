def find_largest_generator(data):
    if not data:
        return
    largest = data[0]
    yield largest
    for item in data[1:]:
        if item > largest:
            largest = item
        yield largest
if __name__ == '__main__':
    sample_list = [10, 5, 40, 2, 99, 33, 1]
    generator = find_largest_generator(sample_list)
    result = []
    for element in generator:
        result.append(element)
    print(result)
    sample_list_2 = [5, 1, 8, 2, 9]
    generator_2 = find_largest_generator(sample_list_2)
    result_2 = []
    for element in generator_2:
        result_2.append(element)
    print(result_2)
    sample_list_3 = [-10, -5, -40, -2, -99]
    generator_3 = find_largest_generator(sample_list_3)
    result_3 = []
    for element in generator_3:
        result_3.append(element)
    print(result_3)
    sample_list_4 = []
    generator_4 = find_largest_generator(sample_list_4)
    result_4 = []
    for element in generator_4:
        result_4.append(element)
    print(result_4)