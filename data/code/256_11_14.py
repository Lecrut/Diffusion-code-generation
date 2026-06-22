def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, -2]
    print(calculate_range(sample_values))