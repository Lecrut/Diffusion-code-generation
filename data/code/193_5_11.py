import numpy as np

def sum_large_numeric_list(numbers):
    return np.sum(numbers)

if __name__ == '__main__':
    sample_numbers = [1000, 2500, 3.5, 4200, -750]
    print("Sample numbers to process:", sample_numbers)
    result = sum_large_numeric_list(sample_numbers)
    print("Total sum:", result)