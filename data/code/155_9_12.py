import numpy as np

def sum_array(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers.")
    return np.array(numbers).sum()

if __name__ == '__main__':
    sample_numbers = [42, 17, 93, 5, 68, 34, 21, 89, 10, 7]
    result = sum_array(sample_numbers)
    print(f"Sum of the numbers: {result}")