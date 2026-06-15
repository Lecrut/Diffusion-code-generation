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
    large_list = [5, 12, 3, 8, 1, 15, 9, 4, 10]
    minimum_values = find_minimum_generator(large_list)
    result_list = list(minimum_values)
    print(result_list)
    another_list = [100, 50, 200, 10]
    minimum_values_2 = find_minimum_generator(another_list)
    result_list_2 = list(minimum_values_2)
    print(result_list_2)
    empty_list = []
    minimum_values_3 = find_minimum_generator(empty_list)
    result_list_3 = list(minimum_values_3)
    print(result_list_3)