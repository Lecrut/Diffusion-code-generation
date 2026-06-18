import numpy as np
def find_differences_numpy(arr1: list | tuple | np.ndarray, arr2: list | tuple | np.ndarray) -> list[int]:
    a = np.array(arr1)
    b = np.array(arr2)
    return [np.where(a != b)[0].tolist()]
def find_differences_python(arr1: list | tuple, arr2: list | tuple) -> list[int]:
    result = []
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            result.append(i)
    return result
if __name__ == '__main__':
    sample_arr_1 = [1, 5, 3, 7, 9]
    sample_arr_2 = [1, 4, 3, 8, 9]
    print("NumPy Result:", find_differences_numpy(sample_arr_1, sample_arr_2))
    print("Python Result:", find_differences_python(sample_arr_1, sample_arr_2))