import numpy as np

def extract_value(arr: np.ndarray, index: tuple) -> int:
    result = arr
    for idx in index:
        result = result[idx]
    return result

if __name__ == '__main__':
    arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    index = (1, 0, 1)
    print(extract_value(arr, index))