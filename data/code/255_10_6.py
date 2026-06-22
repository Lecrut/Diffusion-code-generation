def find_maximum(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value
if __name__ == '__main__':
    sample_values = [10, 5, 22, 8, 30, 1]
    result = find_maximum(sample_values)
    print(result)
    empty_list_result = find_maximum([])
    print(empty_list_result)
    negative_numbers_result = find_maximum([-5, -2, -8, -1])
    print(negative_numbers_result)