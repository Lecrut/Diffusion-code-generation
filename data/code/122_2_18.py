import numpy as np

def validate_input(numbers):
    if not isinstance(numbers, (list, np.ndarray)):
        raise ValueError("Input must be a list or NumPy array of numbers.")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the input must be numbers.")

def compute_average(numbers):
    validate_input(numbers)
    return np.mean(numbers)

if __name__ == '__main__':
    sample_numbers = np.array([10.5, 20.0, 35.5, 15.0])
    average = compute_average(sample_numbers)
    print(average)