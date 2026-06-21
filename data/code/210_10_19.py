def calculate_range(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    range_value = max_value - min_value
    return range_value

if __name__ == '__main__':
    sample_values = [45, 78, 12, 3, 67]
    result = calculate_range(sample_values)
    print(result)