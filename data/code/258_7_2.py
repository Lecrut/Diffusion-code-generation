import numpy as np
def elementwise_average_of_pairs(array1_list, array2_list):
    results = []
    for arr1, arr2 in zip(array1_list, array2_list):
        results.append(np.mean(arr1) + np.mean(arr2))
    return np.array(results)
if __name__ == '__main__':
    array1 = np.array([[1, 2, 3], [4, 5, 6]])
    array2 = np.array([[10, 20, 30], [11, 22, 33]])
    result = elementwise_average_of_pairs(array1, array2)
    print(result)