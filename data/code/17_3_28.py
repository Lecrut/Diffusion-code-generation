def filter_even_numbers(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")
    
    try:
        return [num for num in numbers if isinstance(num, int) and num % 2 == 0]
    except TypeError as e:
        raise ValueError("All elements in the list must be integers.") from e

if __name__ == '__main__':
    sample_values = [10, 15, 22, "33", None, 40, -8, 7.5]
    try:
        even_numbers = filter_even_numbers(sample_values)
        print(even_numbers)
    except ValueError as e:
        print(f"Error: {e}")