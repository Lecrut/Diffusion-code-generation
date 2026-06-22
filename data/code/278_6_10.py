def format_and_print_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be numbers.")
    
    formatted_numbers = [f"{num:.2f}" for num in numbers]
    for number in formatted_numbers:
        print(number)

if __name__ == '__main__':
    sample_values = [3.14159, 2.71828, 0.61803, 1.41421]
    format_and_print_numbers(sample_values)