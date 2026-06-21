import numpy as np

def calculate_sum(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input must be a list of numbers.")
    
    return np.sum(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 25, 3.5, 42]
    try:
        result = calculate_sum(sample_numbers)
        print(f"Total sum: {result}")
    except ValueError as e:
        print(e)