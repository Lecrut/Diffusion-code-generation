import numpy as np

def average_pairs(numbers):
    return np.mean(np.array(numbers).reshape(-1, 2), axis=1)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50, 60]
    print(average_pairs(sample_numbers))