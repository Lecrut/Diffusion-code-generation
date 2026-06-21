def calculate_range(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    
    try:
        min_value = min(numbers)
        max_value = max(numbers)
        return max_value - min_value
    except TypeError:
        raise ValueError("List contains non-numeric types")

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_range(sample_numbers))