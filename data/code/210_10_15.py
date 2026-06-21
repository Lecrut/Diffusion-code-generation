def calculate_range(numbers):
    if not numbers:
        return 0
    minimum = min(numbers)
    maximum = max(numbers)
    data_range = maximum - minimum
    return data_range

if __name__ == '__main__':
    sample_values = [78, 45, 23, 90, 12]
    range_result = calculate_range(sample_values)
    print(range_result)