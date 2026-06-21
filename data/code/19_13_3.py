import numpy as np

def get_random_element(arr):
    idx = np.random.randint(0, arr.size)
    return arr.flat[idx]

if __name__ == '__main__':
    data = np.arange(1000000)
    result = get_random_element(data)
    print(result)