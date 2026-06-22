def find_minimum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    minimum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
    return minimum

if __name__ == '__main__':
    sample_list = [10, 5, 8, 3, 12]
    single_element_list = [42]
    result_multi = find_minimum(sample_list)
    result_single = find_minimum(single_element_list)
    print(result_multi)
    print(result_single)