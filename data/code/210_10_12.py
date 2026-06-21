def calculate_range(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [34, 12, 90, 56, 23]
    print(calculate_range(sample_values))