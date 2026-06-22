def find_min_value(numbers):
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [5, 2, 9, 1, 7]
    single_element_list = [42]
    print(find_min_value(sample_list))
    print(find_min_value(single_element_list))