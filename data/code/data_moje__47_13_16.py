import numpy as np

def calculate_mean(data):
    return np.mean(data)

if __name__ == '__main__':
    test_data = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
    result = calculate_mean(test_data)
    print(result)