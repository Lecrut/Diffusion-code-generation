import numpy as np

def sum_elements(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Invalid input. Only numbers are allowed.")
    return np.sum(np.array(numbers))

if __name__ == '__main__':
    sample_numbers = [10, 25, 3.5, "hello", 42]
    try:
        result = sum_elements(sample_numbers)
        print(f"Total sum: {result}")
    except ValueError as e:
        print(e)