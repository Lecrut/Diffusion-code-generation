def find_minimum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_minimum(sample_list)
    print(result)
    single_element_list = [42]
    single_result = find_minimum(single_element_list)
    print(single_result)