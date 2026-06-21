def calculate_range(numbers):
    if not numbers:
        return 0
    min_num = max_num = numbers[0]
    for num in numbers[1:]:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return max_num - min_num

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    print(calculate_range(sample_values))