import numpy as np

def get_random_element(arr):
    random_index = np.random.randint(0, arr.size)
    return arr.flat[random_index]

if __name__ == '__main__':
    large_array = np.random.rand(1000000)
    print(get_random_element(large_array))