import numpy as np

def calculate_range(data):
    return np.ptp(data)

if __name__ == '__main__':
    sample_data = np.array([3, 5, 1, 2, 4])
    print(calculate_range(sample_data))