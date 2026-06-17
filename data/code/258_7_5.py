import numpy as np
def calculate_pairwise_average(array1, array2):
    if array1.shape != array2.shape:
        raise ValueError("Input arrays must have the same shape")
    return (array1 + array2) / 2
if __name__ == '__main__':
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[10, 20, 30], [40, 50, 60]])
    result = calculate_pairwise_average(arr1, arr2)
    print(result)