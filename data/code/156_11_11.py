import numpy as np

def compute_mean(numbers):
    return np.mean(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    mean_value = compute_mean(sample_values)
    print(mean_value)