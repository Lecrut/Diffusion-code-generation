def calculate_difference(numbers):
    if not all(isinstance(num, float) for num in numbers):
        raise ValueError("All elements in the tuple must be floating-point numbers.")
    
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = (3.5, 7.2, 1.8, 9.4)
    try:
        difference = calculate_difference(sample_values)
        print(difference)
    except ValueError as e:
        print(f"Error: {e}")