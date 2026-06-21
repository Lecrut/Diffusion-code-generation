import numpy as np

def calculate_average(arr):
    return np.mean(arr)

if __name__ == '__main__':
    test_array = np.array([15.2, 23.4, 36.7, 48.9, 50.1])
    average_result = calculate_average(test_array)
    print(average_result)