import numpy as np

def calculate_mean(data_points):
    return np.mean(data_points)

if __name__ == '__main__':
    sample_data = [10.5, 20.3, 15.7, 25.1, 18.9]
    result = calculate_mean(sample_data)
    print(result)