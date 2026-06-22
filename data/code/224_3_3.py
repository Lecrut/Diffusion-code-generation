import numpy as np

def compute_mean(numbers):
    if isinstance(numbers, np.ndarray):
        return np.mean(numbers)
    else:
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(compute_mean(sample_numbers))