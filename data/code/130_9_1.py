import numpy as np
def contains_zero(arr):
    return np.any(arr == 0)
if __name__ == '__main__':
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([1, 0, 3, 4, 5])
    arr3 = np.array([10, 20, 30])
    arr4 = np.array([0, 5, 10])
    arr5 = np.array([[1, 2], [3, 0]])
    arr6 = np.array([])
    print(f"arr1 contains zero: {contains_zero(arr1)}")
    print(f"arr2 contains zero: {contains_zero(arr2)}")
    print(f"arr3 contains zero: {contains_zero(arr3)}")
    print(f"arr4 contains zero: {contains_zero(arr4)}")
    print(f"arr5 contains zero: {contains_zero(arr5)}")
    print(f"arr6 contains zero: {contains_zero(arr6)}")