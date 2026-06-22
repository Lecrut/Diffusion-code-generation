import numpy as np

def find_maximum_value(data):
    return np.max(data)

if __name__ == '__main__':
    sample_data = [45, 23, 67, 89, 34]
    max_value = find_maximum_value(sample_data)
    print(max_value)