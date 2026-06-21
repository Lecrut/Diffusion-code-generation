def calculate_range(numbers):
    if not numbers or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input list must be non-empty and contain only numeric types.")
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_range(sample_numbers))