import numpy as np

def fast_cumulative_sum(data):
    return np.cumsum(data)

if __name__ == '__main__':
    data_points = np.array([10, 20, 30, 40, 50])
    result = fast_cumulative_sum(data_points)
    print(result)