def find_max_with_custom_comparison(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    sample_numbers = [3.14, 2.71, 1.41, 1.73, 0.57, 2.23, 3.00]
    result = find_max_with_custom_comparison(sample_numbers)
    print(result)