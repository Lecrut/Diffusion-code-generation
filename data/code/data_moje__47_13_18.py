import numpy as np

def calculate_mean(data):
    return np.mean(data)

if __name__ == '__main__':
    test_data = np.array([10.5, 20.3, 15.7, 22.1, 18.9])
    result = calculate_mean(test_data)
    print(result)