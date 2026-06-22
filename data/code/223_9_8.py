import numpy as np

MAX_VALUE = None

def find_max_value(data):
    global MAX_VALUE
    if MAX_VALUE is not None:
        return MAX_VALUE
    
    MAX_VALUE = np.max(data)
    return MAX_VALUE

if __name__ == '__main__':
    sample_data = [3, 5, 1, 2, 4]
    print(find_max_value(sample_data))