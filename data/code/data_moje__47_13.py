import numpy as np

def calculate_mean(data_points):
    return np.mean(data_points)

if __name__ == '__main__':
    test_data = [10.5, 12.3, 9.8, 14.2, 11.0, 8.5, 13.7, 10.9]
    result = calculate_mean(test_data)
    print(result)