import numpy as np

def calculate_average(numbers):
    if not numbers:
        return 0.0
    numbers = np.array(numbers, dtype=np.float64)
    average = np.mean(numbers)
    return average

if __name__ == '__main__':
    sample_numbers = [10.5, 20.0, 35.5, 15.0]
    average = calculate_average(sample_numbers)
    print(average)