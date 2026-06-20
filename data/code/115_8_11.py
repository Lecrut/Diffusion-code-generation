import numpy as np

class ArrayDivider:
    @staticmethod
    def divide_arrays(a, b):
        return np.where(b != 0, a / b, 0)

if __name__ == '__main__':
    array1 = np.array([10, 20, 30, 40])
    array2 = np.array([2, 0, 5, 0])
    division_result = ArrayDivider.divide_arrays(array1, array2)
    print(division_result)