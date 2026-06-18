def find_max(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value
if __name__ == '__main__':
    sample_list = [3, 7, 2, 9, 4, 85, 1]
    result = find_max(sample_list)
    print(result)