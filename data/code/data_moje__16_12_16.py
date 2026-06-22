import numpy as np

def get_first_element(arr: np.ndarray) -> any:
    return arr.flat[0]

if __name__ == '__main__':
    data = np.array([[1, 2], [3, 4], [5, 6]])
    result = get_first_element(data)
    print(result)