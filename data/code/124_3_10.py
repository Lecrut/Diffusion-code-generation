import numpy as np

def perform_arithmetic_operations(list1, list2):
    if not all(isinstance(x, (int, float)) for x in list1 + list2):
        raise ValueError("Both lists must contain only numbers.")
    
    array1 = np.array(list1)
    array2 = np.array(list2)
    
    addition_result = array1 + array2
    subtraction_result = array1 - array2
    multiplication_result = array1 * array2
    division_result = array1 / array2
    
    return addition_result, subtraction_result, multiplication_result, division_result

if __name__ == '__main__':
    list1 = [10, 20]
    list2 = [5, 3]
    
    try:
        addition, subtraction, multiplication, division = perform_arithmetic_operations(list1, list2)
        print("Addition:", addition)
        print("Subtraction:", subtraction)
        print("Multiplication:", multiplication)
        print("Division:", division)
    except ValueError as e:
        print(e)