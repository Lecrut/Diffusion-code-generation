def find_min_max(numbers):
    min_num = float('inf')
    max_num = float('-inf')
    for num in numbers:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return min_num, max_num

if __name__ == '__main__':
    sample_numbers = [34, 12, 98, 76, 54, 23, 67, 89, 0, -1]
    min_val, max_val = find_min_max(sample_numbers)
    print(f"Minimum: {min_val}, Maximum: {max_val}")