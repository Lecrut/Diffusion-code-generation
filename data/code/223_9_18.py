import numpy as np

def find_max_value(data):
    return np.max(data)

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    max_value = find_max_value(sample_data)
    print(max_value)