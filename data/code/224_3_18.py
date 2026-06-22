import numpy as np

def calculate_average(numbers):
    if isinstance(numbers, np.ndarray):
        return np.mean(numbers)
    else:
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10.5, 20.3, 30.7, 40.2, 50.8]
    result = calculate_average(sample_numbers)
    print(result)