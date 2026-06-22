import numpy as np

def calculate_mean(data):
    if len(data) == 0:
        return 0.0
    return np.mean(data)

if __name__ == '__main__':
    test_data = [10.5, 20.3, 30.7, 40.1, 50.2]
    result = calculate_mean(test_data)
    print(result)