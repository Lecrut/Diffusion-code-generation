import numpy as np

def sum_large_list(numbers):
    return np.sum(numbers)

if __name__ == '__main__':
    sample_numbers = list(range(1000000))
    print(sum_large_list(sample_numbers))