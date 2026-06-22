def calculate_range(numbers):
    if not numbers:
        return 0.0
    minimum = min(numbers)
    maximum = max(numbers)
    range_value = maximum - minimum
    return range_value

if __name__ == '__main__':
    sample_data = [10.5, 3.2, 8.8, 1.1, 5.0]
    print(calculate_range(sample_data))