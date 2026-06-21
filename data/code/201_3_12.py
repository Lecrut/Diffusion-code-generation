import numpy as np

def compute_array_mean(arr):
    return np.mean(arr)

if __name__ == '__main__':
    sample_data = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
    result = compute_array_mean(sample_data)
    print(result)