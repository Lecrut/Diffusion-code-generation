import numpy as np

def find_range(data):
    return np.max(data) - np.min(data)

if __name__ == '__main__':
    sample_data = np.array([3, 5, 1, 2, 4])
    print(find_range(sample_data))