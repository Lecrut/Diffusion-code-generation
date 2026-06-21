import numpy as np

def calculate_mean(data):
    return np.mean(data)

if __name__ == '__main__':
    data_points = [100, 200, 300]
    mean_value = calculate_mean(data_points)
    print(mean_value)