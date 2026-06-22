def find_minimum(numbers):
    if not numbers:
        return None
    minimum_value = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < minimum_value:
            minimum_value = numbers[i]
    return minimum_value

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9]
    result = find_minimum(sample_list)
    print(result)
    single_element_list = [42]
    single_result = find_minimum(single_element_list)
    print(single_result)