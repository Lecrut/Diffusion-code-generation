import numpy as np

def calculate_mean(data_points):
    return np.mean(data_points)

if __name__ == '__main__':
    sample_data = [10.5, 23.7, 15.2, 40.1, 18.9, 32.6, 27.4, 12.3, 35.8, 19.5]
    result = calculate_mean(sample_data)
    print(result)