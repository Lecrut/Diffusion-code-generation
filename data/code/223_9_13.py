import numpy as np

MAX_THRESHOLD = 10**9

def find_max_value(data):
    return np.max(data)

if __name__ == '__main__':
    sample_data = [3, 5, 1, 2, 4]
    print(find_max_value(sample_data))