import numpy as np

def calculate_mean(data):
    array = np.array(data)
    return np.mean(array)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = calculate_mean(sample_data)
    print(result)