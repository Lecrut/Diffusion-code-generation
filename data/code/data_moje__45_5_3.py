def find_minimum(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not numbers:
        raise ValueError("List must not be empty")
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [5, 3, 9, 1, 7]
    result = find_minimum(sample_list)
    print(result)