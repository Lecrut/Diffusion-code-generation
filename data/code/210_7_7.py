def calculate_range(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("The list contains non-numeric types")
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_range(sample_numbers))