import numpy as np

def get_random_element(arr: np.ndarray) -> np.number:
    idx = np.random.randint(0, arr.size)
    return arr.flat[idx]

if __name__ == '__main__':
    sample_array = np.arange(1000000)
    result = get_random_element(sample_array)
    print(result)