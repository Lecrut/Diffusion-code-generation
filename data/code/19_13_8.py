import numpy as np

def get_random_element(arr):
    return arr[np.random.randint(0, arr.size)]

if __name__ == '__main__':
    large_array = np.arange(10000)
    result = get_random_element(large_array)
    print(result)