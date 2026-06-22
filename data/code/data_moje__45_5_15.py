def get_minimum(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    if len(numbers) == 0:
        raise ValueError("List must contain at least one number")
    min_val = numbers[0]
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be numbers")
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    result = get_minimum(sample_data)
    print(result)