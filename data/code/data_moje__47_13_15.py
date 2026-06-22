import numpy as np

def calculate_mean(data_points):
    return np.mean(data_points)

if __name__ == '__main__':
    test_data = [10, 20, 30, 40, 50]
    result = calculate_mean(test_data)
    print(result)