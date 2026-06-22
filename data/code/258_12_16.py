import numpy as np

def average_pairs(numbers):
    return np.mean(np.array(numbers).reshape(-1, 2), axis=1)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6]
    print(average_pairs(sample_values))