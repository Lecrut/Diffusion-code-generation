import numpy as np
def calculate_elementwise_average(array1_list, array2_list):
    results = []
    for arr1, arr2 in zip(array1_list, array2_list):
        results.append((arr1 + arr2) / 2.0)
    return np.array(results)
if __name__ == '__main__':
    array1_data = [np.array([1.0, 2.0, 3.0]), np.array([4.0, 5.0, 6.0])]
    array2_data = [np.array([7.0, 8.0, 9.0]), np.array([10.0, 11.0, 12.0])]
    average_result = calculate_elementwise_average(array1_data, array2_data)
    print(average_result)