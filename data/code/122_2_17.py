import numpy as np

def compute_average(numbers):
    numbers = np.array(numbers)
    count = np.count_nonzero(numbers)
    if count == 0:
        return 0.0
    sum_values = np.sum(numbers)
    average = sum_values / count
    return average

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5]
    print(compute_average(sample_numbers))