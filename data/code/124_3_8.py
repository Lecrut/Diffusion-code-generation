import numpy as np
LIST1 = [10, 20]
LIST2 = [5, 3]

def perform_arithmetic_operations(list1=LIST1, list2=LIST2):
    array1 = np.array(list1)
    array2 = np.array(list2)
    addition_result = array1 + array2
    subtraction_result = array1 - array2
    multiplication_result = array1 * array2
    division_result = array1 / array2
    return (addition_result, subtraction_result, multiplication_result, division_result)
if __name__ == '__main__':
    addition, subtraction, multiplication, division = perform_arithmetic_operations()
    print('Addition:', addition)
    print('Subtraction:', subtraction)
    print('Multiplication:', multiplication)
    print('Division:', division)