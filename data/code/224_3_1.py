import numpy as np

def compute_mean(numbers):
    if isinstance(numbers, np.ndarray):
        return np.mean(numbers)
    else:
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5]
    print(compute_mean(sample_numbers))