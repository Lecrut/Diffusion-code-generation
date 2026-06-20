import numpy as np

def perform_arithmetic_operations(list1, list2):
    array1 = np.array(list1)
    array2 = np.array(list2)
    addition_result = array1 + array2
    subtraction_result = array1 - array2
    multiplication_result = array1 * array2
    division_result = array1 / array2
    return addition_result, subtraction_result, multiplication_result, division_result

if __name__ == '__main__':
    sample_list1 = [100, 200]
    sample_list2 = [10, 5]
    result_addition, result_subtraction, result_multiplication, result_division = perform_arithmetic_operations(sample_list1, sample_list2)
    print("Addition:", result_addition)
    print("Subtraction:", result_subtraction)
    print("Multiplication:", result_multiplication)
    print("Division:", result_division)