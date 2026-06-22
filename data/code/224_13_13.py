import numpy as np

def calculate_mean(arr):
    return np.mean(arr)

if __name__ == '__main__':
    sample_array = [4, 8, 12, 16]
    print(calculate_mean(sample_array))