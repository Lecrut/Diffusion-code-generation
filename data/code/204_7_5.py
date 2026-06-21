import numpy as np

def compute_middle_value(numbers):
    return np.median(numbers)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(compute_middle_value(sample_values))