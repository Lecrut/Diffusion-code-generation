import numpy as np

def get_random_element(arr: np.ndarray) -> np.generic:
    idx = np.random.randint(0, arr.size)
    return arr.flat[idx]

if __name__ == '__main__':
    arr = np.arange(10000)
    result = get_random_element(arr)
    print(result)