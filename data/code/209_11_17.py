import numpy as np

def compute_average(data):
    return float(np.mean(data))

if __name__ == '__main__':
    data_points = [15, 25, 35, 45, 55]
    average_result = compute_average(data_points)
    print(average_result)