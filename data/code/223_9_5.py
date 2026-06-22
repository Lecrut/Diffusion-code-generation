import numpy as np

def find_max_value(data):
    return np.max(data)

if __name__ == '__main__':
    sample_data = [45, 12, 78, 36, 90]
    result = find_max_value(sample_data)
    print(result)