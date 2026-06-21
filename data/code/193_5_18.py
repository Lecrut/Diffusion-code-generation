import numpy as np

def validate_input(numbers):
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError(f"Invalid input '{num}'. Only numbers are allowed.")
    return True

def calculate_sum(numbers):
    if not validate_input(numbers):
        return None
    return np.sum(np.array(numbers))

if __name__ == '__main__':
    sample_numbers = [10, 25, 3.5, "hello", 42]
    print("Sample numbers to process:", sample_numbers)
    result = calculate_sum(sample_numbers)
    if result is not None:
        print("Total sum:", result)