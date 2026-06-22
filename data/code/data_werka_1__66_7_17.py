def compare_adjacent_ascending(data):
    if not all((isinstance(x, (int, float)) for x in data)):
        raise TypeError('All elements must be integers or floats.')
    return [data[i] < data[i + 1] for i in range(len(data) - 1)]
if __name__ == '__main__':
    test_data_1 = [1, 2, 3, 4]
    test_data_2 = [1, 2, 'a', 4]
    test_data_3 = [1.5, 1.5, 2.5]
    test_data_4 = [1, 2, 3, 'b']
    test_data_5 = [1, 2, 3, 4, 5]
    try:
        print(compare_adjacent_ascending(test_data_1))
    except TypeError as e:
        print(e)
    try:
        print(compare_adjacent_ascending(test_data_2))
    except TypeError as e:
        print(e)
    try:
        print(compare_adjacent_ascending(test_data_3))
    except TypeError as e:
        print(e)
    try:
        print(compare_adjacent_ascending(test_data_4))
    except TypeError as e:
        print(e)
    try:
        print(compare_adjacent_ascending(test_data_5))
    except TypeError as e:
        print(e)