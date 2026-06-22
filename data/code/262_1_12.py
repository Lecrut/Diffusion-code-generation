def find_min_max(numbers):
    if not numbers:
        return None, None
    min_num = max_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return min_num, max_num

if __name__ == '__main__':
    sample_numbers = [3.14, 2.71, 0.57, 1.618, -1.414]
    min_val, max_val = find_min_max(sample_numbers)
    print(f"Minimum: {min_val}, Maximum: {max_val}")