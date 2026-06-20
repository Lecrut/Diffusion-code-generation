import numpy as np

def divide_by_scalar(numbers, divisor):
    if not isinstance(numbers, np.ndarray) or not numbers.ndim == 1:
        raise ValueError("Input must be a one-dimensional NumPy array.")
    if not isinstance(divisor, (int, float)):
        raise TypeError("Divisor must be an integer or a float.")
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    
    return numbers / divisor

if __name__ == '__main__':
    sample_numbers = np.array([12, 45, 67, 89, 23])
    scalar_divisor = 3
    result = divide_by_scalar(sample_numbers, scalar_divisor)
    print(result)