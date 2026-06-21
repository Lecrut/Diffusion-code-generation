def calculate_range(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    try:
        return max(numbers) - min(numbers)
    except TypeError:
        raise ValueError("The list contains non-numeric types")

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(calculate_range(sample_numbers))