def calculate_range_difference(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    print(calculate_range_difference(sample_values))