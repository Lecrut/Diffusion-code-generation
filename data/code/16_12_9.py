import numpy as np

def get_first_element(arr: np.ndarray) -> int:
    return arr[0]

if __name__ == '__main__':
    data = np.array([10, 20, 30, 40, 50])
    result = get_first_element(data)
    print(result)