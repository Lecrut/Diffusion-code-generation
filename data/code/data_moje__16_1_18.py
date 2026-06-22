import numpy as np

def extract_initial_value(arr):
    flat = np.asarray(arr).ravel()
    return flat[0]

if __name__ == '__main__':
    sample = np.array([[1, 2], [3, 4]])
    result = extract_initial_value(sample)
    print(result)