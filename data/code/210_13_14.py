def calculate_range(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num - min_num

if __name__ == '__main__':
    sample_numbers = [12, 34, 56, 78, 90]
    result = calculate_range(sample_numbers)
    print(result)