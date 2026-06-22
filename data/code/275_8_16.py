def find_max_min(numbers):
    if not numbers:
        return None, None
    max_val = min_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
    return max_val, min_val

if __name__ == '__main__':
    sample_numbers = [4, 9, 2, 7, 5]
    result_max, result_min = find_max_min(sample_numbers)
    print(f"Max: {result_max}, Min: {result_min}")