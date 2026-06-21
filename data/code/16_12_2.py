import numpy as np

def get_first_element(array):
    return array.flat[0]

if __name__ == '__main__':
    sample_data = np.array([10, 20, 30, 40, 50])
    result = get_first_element(sample_data)
    print(result)