def compare_elements(data, index_first, index_second):
    LOWER_BOUND = 0
    COMPARISON_GREATER = "greater than"
    COMPARISON_LESS = "less than"
    COMPARISON_EQUAL = "equal"
    RESULT_OUT_OF_BOUNDS = "index out of bounds"

    if not isinstance(data, list):
        raise ValueError("First argument must be a list")

    data_length = len(data)
    is_first_valid = LOWER_BOUND <= index_first < data_length
    is_second_valid = LOWER_BOUND <= index_second < data_length

    if not is_first_valid or not is_second_valid:
        return RESULT_OUT_OF_BOUNDS

    element_first = data[index_first]
    element_second = data[index_second]

    if element_first > element_second:
        return COMPARISON_GREATER
    if element_first < element_second:
        return COMPARISON_LESS
    return COMPARISON_EQUAL

if __name__ == '__main__':
    test_array = [100, 25, 50, 75, 10]
    first_result = compare_elements(test_array, 0, 1)
    print(first_result)
    second_result = compare_elements(test_array, 2, 3)
    print(second_result)
    third_result = compare_elements(test_array, 5, 1)
    print(third_result)
    fourth_result = compare_elements(test_array, -1, 0)
    print(fourth_result)
    fifth_result = compare_elements(test_array, 0, 0)
    print(fifth_result)