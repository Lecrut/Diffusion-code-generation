import numpy as np

def extract_elements(array, indices):
    return array[indices]
if __name__ == '__main__':
    data_array = np.array([100, 200, 300, 400, 500])
    index_array = np.array([1, 3, 4])
    result = extract_elements(data_array, index_array)
    print(result)