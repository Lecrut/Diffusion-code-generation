def find_min_max(numbers):
    min_num = max_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return min_num, max_num

if __name__ == '__main__':
    sample_data = [3456789, 1234567, 9876543, 24680, 13579]
    min_val, max_val = find_min_max(sample_data)
    print(f"Minimum: {min_val}, Maximum: {max_val}")