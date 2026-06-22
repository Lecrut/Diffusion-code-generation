import numpy as np

def get_middle_element(arr: np.ndarray) -> float:
    if arr.ndim != 1:
        raise ValueError("Input array must be 1-dimensional")
    if arr.size == 0:
        raise ValueError("Input array cannot be empty")
    mid_index = arr.size // 2
    if arr.size % 2 == 0:
        return (arr[mid_index - 1] + arr[mid_index]) / 2.0
    return float(arr[mid_index])

if __name__ == '__main__':
    sample_odd = np.array([1, 3, 5, 7, 9])
    sample_even = np.array([1, 2, 3, 4])
    print(get_middle_element(sample_odd))
    print(get_middle_element(sample_even))