def find_minimum(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    min_val = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min_val:
            min_val = numbers[i]
    return min_val

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_minimum(sample_list)
    print(result)
    
    single_element_list = [42]
    single_result = find_minimum(single_element_list)
    print(single_result)