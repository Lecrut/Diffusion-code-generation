import numpy as np

def extract_value(arr: np.ndarray, indices: tuple) -> float:
    idx = tuple(np.asarray(indices) % np.asarray(arr.shape))
    return arr[idx].item()

if __name__ == '__main__':
    data = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    result = extract_value(data, (1, 0, 1))
    print(result)