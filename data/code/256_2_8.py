def calculate_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 1.2, 4.8, 2.9, 0.7]
    print(calculate_range(sample_numbers))