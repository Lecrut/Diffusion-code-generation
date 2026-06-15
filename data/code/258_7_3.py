import numpy as np
def calculate_pairwise_average(arr1_list, arr2_list):
    result_list = []
    for arr1, arr2 in zip(arr1_list, arr2_list):
        result_list.append((arr1 + arr2) / 2.0)
    return np.array(result_list)
if __name__ == '__main__':
    np.random.seed(42)
    arr1 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    arr2 = np.array([[10.0, 20.0, 30.0], [1.0, 2.0, 3.0]])
    result = calculate_pairwise_average(arr1, arr2)
    print(result)