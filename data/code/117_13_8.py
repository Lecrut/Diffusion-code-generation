import numpy as np

def calculate_difference():
    a = np.array([i for i in range(10000)])
    b = np.array([i*2 for i in range(10000)])
    return np.subtract(b, a)

if __name__ == '__main__':
    result = calculate_difference()
    print(result)