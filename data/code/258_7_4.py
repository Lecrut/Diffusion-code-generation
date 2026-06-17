import numpy as np
def elementwise_average_of_pairs(arr1_list, arr2_list):
    results = []
    for arr1, arr2 in zip(arr1_list, arr2_list):
        results.append(np.mean(arr1) + np.mean(arr2))
    return np.array(results)
if __name__ == '__main__':
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[10, 20, 30], [11, 22, 33]])
    result = elementwise_average_of_pairs(arr1, arr2)
    print(result)