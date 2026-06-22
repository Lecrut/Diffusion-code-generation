def find_minimum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    if not numbers:
        return None
    min_value = numbers[0]
    for num in numbers[1:]:
        if num < min_value:
            min_value = num
    return min_value

if __name__ == '__main__':
    sample_list = [5, 2, 9, 1, 7]
    single_element_list = [42]
    empty_list = []

    result_multi = find_minimum(sample_list)
    result_single = find_minimum(single_element_list)
    result_empty = find_minimum(empty_list)

    print(result_multi)
    print(result_single)
    print(result_empty)