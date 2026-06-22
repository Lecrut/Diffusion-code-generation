import numpy as np

def calculate_mean(data):
    return np.mean(data)

if __name__ == '__main__':
    test_data = [10, 20, 30, 40, 50]
    mean_value = calculate_mean(test_data)
    print(mean_value)