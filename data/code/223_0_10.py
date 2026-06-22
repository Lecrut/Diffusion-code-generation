def find_max_value(numbers):
    return max(numbers)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    result1 = find_max_value(sample_list)
    print(f"Maximum of {sample_list}: {result1}")

    another_sample_list = [-10, -5, -20, -1]
    result2 = find_max_value(another_sample_list)
    print(f"Maximum of {another_sample_list}: {result2}")

    single_element_list = [7]
    result3 = find_max_value(single_element_list)
    print(f"Maximum of {single_element_list}: {result3}")

    empty_list = []
    try:
        result4 = find_max_value(empty_list)
    except ValueError as e:
        print(e)