import numpy as np

def calculate_mean(data_points):
    if not data_points:
        raise ValueError("Data points list cannot be empty")
    return np.mean(data_points)

if __name__ == '__main__':
    test_data = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11]
    result = calculate_mean(test_data)
    print(result)