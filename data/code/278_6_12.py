def format_and_print_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be numbers.")
    
    for number in numbers:
        print(f"{number:.2f}")

if __name__ == '__main__':
    sample_numbers = [3.14159, 2.71828, 0.00123, 100.0]
    format_and_print_numbers(sample_numbers)