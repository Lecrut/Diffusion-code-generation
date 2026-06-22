import numpy as np

def calculate_mean(data):
    return np.mean(data)

if __name__ == '__main__':
    test_data = np.array([10, 20, 30, 40, 50])
    result = calculate_mean(test_data)
    print(result)