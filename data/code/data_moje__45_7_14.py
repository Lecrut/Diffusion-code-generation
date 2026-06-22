def find_minimum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9]
    single_element_list = [42]
    print(find_minimum(sample_list))
    print(find_minimum(single_element_list))