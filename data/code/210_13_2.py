def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(calculate_range(sample_values))