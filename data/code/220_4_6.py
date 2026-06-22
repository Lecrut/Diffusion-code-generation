def calculate_average(numbers):
    if not numbers:
        raise ValueError("The sequence is empty")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numbers")
    
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10.5, 20.3, 30.7]
    print(calculate_average(sample_numbers))