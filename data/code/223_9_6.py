import numpy as np

def find_max_value(data):
    return np.max(data)

if __name__ == '__main__':
    sample_data = [10, 5, 20, 8, 15]
    print(find_max_value(sample_data))