import numpy as np

def extract_value(arr: np.ndarray, index: tuple) -> float:
    return arr[index]

if __name__ == '__main__':
    array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    idx = (1, 0, 1)
    result = extract_value(array, idx)
    print(result)