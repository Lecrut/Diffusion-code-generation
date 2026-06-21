import numpy as np

def compute_mean(numbers):
    return np.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(compute_mean(sample_numbers))