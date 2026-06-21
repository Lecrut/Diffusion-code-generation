import numpy as np

def calculate_min_max(data):
    return np.min(data), np.max(data)

if __name__ == '__main__':
    sample_data = np.array([3, 5, 1, 2, 4])
    min_val, max_val = calculate_min_max(sample_data)
    print(f"Minimum: {min_val}, Maximum: {max_val}")