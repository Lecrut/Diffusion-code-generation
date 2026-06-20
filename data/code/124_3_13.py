import numpy as np

def perform_arithmetic_operations():
    list1 = [10, 20]
    list2 = [5, 3]
    array1 = np.array(list1)
    array2 = np.array(list2)
    operations = {
        'addition': array1 + array2,
        'subtraction': array1 - array2,
        'multiplication': array1 * array2,
        'division': array1 / array2
    }
    return operations

if __name__ == '__main__':
    results = perform_arithmetic_operations()
    print("Addition:", results['addition'])
    print("Subtraction:", results['subtraction'])
    print("Multiplication:", results['multiplication'])
    print("Division:", results['division'])