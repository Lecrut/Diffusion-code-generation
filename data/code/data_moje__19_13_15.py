import numpy as np

def get_random_element(arr):
    idx = np.random.randint(0, arr.size)
    return arr[idx]

if __name__ == '__main__':
    large_array = np.arange(1000000)
    result = get_random_element(large_array)
    print(result)