def calculate_range(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List contains non-numeric types")
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(calculate_range(sample_values))