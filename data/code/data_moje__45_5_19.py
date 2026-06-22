def find_minimum(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) == 0:
        raise ValueError("List must not be empty")
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [34, 15, 88, 2, 99]
    result = find_minimum(sample_list)
    print(result)