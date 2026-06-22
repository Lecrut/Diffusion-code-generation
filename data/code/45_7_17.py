def find_minimum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [4, 2, 9, 1, 7, 3]
    single_element_list = [42]
    result1 = find_minimum(sample_list)
    result2 = find_minimum(single_element_list)
    print(result1)
    print(result2)