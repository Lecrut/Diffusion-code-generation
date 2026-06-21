import numpy as np

def calculate_sum(numbers):
    return np.sum(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 25, 3.5, 42]
    result = calculate_sum(sample_numbers)
    print("Total sum:", result)