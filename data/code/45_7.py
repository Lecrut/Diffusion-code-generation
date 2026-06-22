def find_minimum(numbers):
    if not numbers:
        return None
    minimum_value = numbers[0]
    index = 1
    while index < len(numbers):
        if numbers[index] < minimum_value:
            minimum_value = numbers[index]
        index += 1
    return minimum_value

if __name__ == '__main__':
    sample_list = [5, 2, 9, 1, 7]
    single_element_list = [42]
    result1 = find_minimum(sample_list)
    result2 = find_minimum(single_element_list)
    print(result1)
    print(result2)