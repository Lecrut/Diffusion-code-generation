import numpy as np

def get_random_element(arr):
    if arr.size == 0:
        raise ValueError("Array must not be empty")
    idx = np.random.randint(0, arr.size)
    return arr[idx]

if __name__ == '__main__':
    sample_data = np.random.rand(1000000)
    result = get_random_element(sample_data)
    print(result)