def calculate_mean(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers.")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 5.0]
    print(calculate_mean(sample_values))