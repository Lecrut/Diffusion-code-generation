def calculate_range(numbers):
    if not numbers:
        raise ValueError("No numbers provided.")
    
    minimum = min(numbers)
    maximum = max(numbers)
    return maximum - minimum

if __name__ == '__main__':
    sample_numbers = [10, 5, 22, 8, 15]
    try:
        result = calculate_range(sample_numbers)
        print(result)
    except ValueError as e:
        print(e)