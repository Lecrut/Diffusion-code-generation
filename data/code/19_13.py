import numpy as np

def get_random_element(arr):
    if arr.size == 0:
        raise ValueError("Array is empty")
    index = np.random.randint(0, arr.size)
    return arr[index]

if __name__ == '__main__':
    large_array = np.arange(10000000, dtype=np.float64)
    random_val = get_random_element(large_array)
    print(random_val)