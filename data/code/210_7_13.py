def calculate_range(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("List contains non-numeric types")
    
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(calculate_range(sample_values))