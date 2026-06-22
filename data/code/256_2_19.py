def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 1.9, 5.0]
    print(calculate_range(sample_numbers))