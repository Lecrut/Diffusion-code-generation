def find_minimum(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    index = 1
    while index < len(numbers):
        if numbers[index] < minimum:
            minimum = numbers[index]
        index += 1
    return minimum

if __name__ == '__main__':
    sample_list_single = [42]
    sample_list_multiple = [5, 2, 9, 1, 7]
    sample_list_empty = []
    result_single = find_minimum(sample_list_single)
    result_multiple = find_minimum(sample_list_multiple)
    result_empty = find_minimum(sample_list_empty)
    print(result_single)
    print(result_multiple)
    print(result_empty)