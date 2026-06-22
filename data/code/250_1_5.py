import numpy as np

def calculate_average(arr):
    return np.mean(arr)

if __name__ == '__main__':
    sample_array = np.array([10, 20, 30, 40, 50])
    print(calculate_average(sample_array))