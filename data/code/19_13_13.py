import numpy as np

def get_random_element(array):
    if array.size == 0:
        raise ValueError("Array must not be empty")
    index = np.random.randint(0, array.size)
    return array.flat[index]

if __name__ == '__main__':
    sample_array = np.arange(1000)
    result = get_random_element(sample_array)
    print(result)