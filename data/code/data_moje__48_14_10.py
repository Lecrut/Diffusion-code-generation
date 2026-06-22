def find_custom_max(numbers):
    if not numbers:
        raise ValueError("Array must not be empty")
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    sample_numbers = [3.14, 2.71, 1.41, 1.73, 0.577]
    result = find_custom_max(sample_numbers)
    print(result)