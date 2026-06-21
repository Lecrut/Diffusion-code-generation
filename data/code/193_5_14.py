import numpy as np

def validate_input(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Invalid input. Only numbers are allowed.")

def calculate_sum(numbers):
    validate_input(numbers)
    return np.sum(np.array(numbers))

if __name__ == '__main__':
    sample_numbers = [10, 25, 3.5, "hello", 42]
    try:
        result = calculate_sum(sample_numbers)
        print("Total sum:", result)
    except ValueError as e:
        print(e)