def find_largest_generator(data):
    if not data:
        return
    largest = data[0]
    yield largest
    for element in data[1:]:
        if element > largest:
            largest = element
        yield largest
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 8, 7]
    generator = find_largest_generator(sample_list)
    result = []
    for item in generator:
        result.append(item)
    print(result)
    sample_list_2 = [100, 50, 200, 10]
    generator_2 = find_largest_generator(sample_list_2)
    result_2 = []
    for item in generator_2:
        result_2.append(item)
    print(result_2)
    sample_list_3 = [-5, -1, -10]
    generator_3 = find_largest_generator(sample_list_3)
    result_3 = []
    for item in generator_3:
        result_3.append(item)
    print(result_3)
    sample_list_4 = []
    generator_4 = find_largest_generator(sample_list_4)
    result_4 = []
    for item in generator_4:
        result_4.append(item)
    print(result_4)