def calculate_range(numbers):
    if not numbers:
        return 0.0
    min_value = min(numbers)
    max_value = max(numbers)
    return max_value - min_value
if __name__ == '__main__':
    sample_data = [10.5, 2.1, 8.0, 4.9, 15.7]
    print(calculate_range(sample_data))