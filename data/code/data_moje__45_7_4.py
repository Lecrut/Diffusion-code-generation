def find_minimum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [5, 2, 9, 1, 7]
    print(find_minimum(sample_list))
    single_element_list = [42]
    print(find_minimum(single_element_list))