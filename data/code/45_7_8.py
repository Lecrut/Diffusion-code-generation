def find_minimum(numbers):
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")
    min_value = numbers[0]
    for num in numbers[1:]:
        if num < min_value:
            min_value = num
    return min_value

if __name__ == '__main__':
    sample_list = [5, 2, 9, 1, 7]
    result = find_minimum(sample_list)
    print(result)
    single_element_list = [42]
    single_result = find_minimum(single_element_list)
    print(single_result)