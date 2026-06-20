import numpy as np

def perform_elementwise_operations(list1, list2):
    array1 = np.array(list1)
    array2 = np.array(list2)
    addition_result = array1 + array2
    subtraction_result = array1 - array2
    multiplication_result = array1 * array2
    division_result = array1 / array2
    return addition_result, subtraction_result, multiplication_result, division_result

if __name__ == '__main__':
    sample_list1 = [10, 20]
    sample_list2 = [5, 3]
    results = perform_elementwise_operations(sample_list1, sample_list2)
    print("Addition:", results[0])
    print("Subtraction:", results[1])
    print("Multiplication:", results[2])
    print("Division:", results[3])