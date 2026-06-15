def find_minimum_generator(data):
    if not data:
        return
    current_min = data[0]
    yield current_min
    for item in data[1:]:
        if item < current_min:
            current_min = item
            yield current_min
if __name__ == '__main__':
    large_list = [5, 12, 3, 8, 1, 15, -2, 9, 0, 4]
    minimum_values = find_minimum_generator(large_list)
    result = []
    for min_val in minimum_values:
        result.append(min_val)
    print(result)
    another_list = [100, 50, 200, 10]
    minimum_values_2 = find_minimum_generator(another_list)
    result_2 = []
    for min_val in minimum_values_2:
        result_2.append(min_val)
    print(result_2)
    empty_list = []
    minimum_values_3 = find_minimum_generator(empty_list)
    result_3 = []
    for min_val in minimum_values_3:
        result_3.append(min_val)
    print(result_3)