def calculate_range(numbers):
    if not numbers:
        return 0.0
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [10.5, 2.1, 8.0, 4.9, 15.7]
    print(calculate_range(sample_values))