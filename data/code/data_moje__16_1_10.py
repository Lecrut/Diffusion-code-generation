import numpy as np

def extract_initial_value(arr):
    if not isinstance(arr, np.ndarray):
        arr = np.array(arr)
    if arr.size == 0:
        return None
    return arr.flat[0]

if __name__ == '__main__':
    sample_array = np.array([[1, 2, 3], [4, 5, 6]])
    result = extract_initial_value(sample_array)
    print(result)

    sample_array_2 = np.array([10, 20, 30])
    result_2 = extract_initial_value(sample_array_2)
    print(result_2)

    sample_array_3 = np.array([])
    result_3 = extract_initial_value(sample_array_3)
    print(result_3)

    sample_array_4 = np.array(42)
    result_4 = extract_initial_value(sample_array_4)
    print(result_4)