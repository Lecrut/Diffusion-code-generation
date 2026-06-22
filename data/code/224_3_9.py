import numpy as np

def compute_mean(numbers):
    if isinstance(numbers, np.ndarray) and numbers.dtype == np.float64:
        return np.mean(numbers)
    else:
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [1.2, 3.4, 5.6, 7.8]
    mean_value = compute_mean(sample_numbers)
    print(f"The mean of {sample_numbers} is {mean_value}")