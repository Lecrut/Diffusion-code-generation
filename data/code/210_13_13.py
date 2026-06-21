def validate_numbers(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be numbers")

def calculate_range(numbers):
    validate_numbers(numbers)
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, 2]
    print(calculate_range(sample_numbers))