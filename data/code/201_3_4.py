import numpy as np

def calculate_mean(values):
    return np.mean(values)

if __name__ == '__main__':
    test_array = np.array([10.5, 20.3, 30.7, 40.2, 50.1])
    result = calculate_mean(test_array)
    print(result)