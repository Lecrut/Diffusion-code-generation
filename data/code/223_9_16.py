import numpy as np

def find_max_value(data):
    return np.max(data)

if __name__ == '__main__':
    sample_data = [3, 5, 2, 8, 1, 9]
    print(find_max_value(sample_data))