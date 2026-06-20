import numpy as np

def compute_average(numbers):
    if not numbers:
        return 0.0
    total = np.sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_numbers = [12.5, 23.0, 34.5, 17.0]
    avg = compute_average(sample_numbers)
    print(avg)