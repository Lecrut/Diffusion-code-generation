import numpy as np
def contains_zero(arr):
    return np.any(arr == 0)
if __name__ == '__main__':
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([1, 0, 3, 4, 5])
    arr3 = np.array([10, 20, 30])
    arr4 = np.array([0, 5, 10])
    arr5 = np.array([[1, 2], [3, 0]])
    print(f"Array 1 contains zero: {contains_zero(arr1)}")
    print(f"Array 2 contains zero: {contains_zero(arr2)}")
    print(f"Array 3 contains zero: {contains_zero(arr3)}")
    print(f"Array 4 contains zero: {contains_zero(arr4)}")
    print(f"Array 5 contains zero: {contains_zero(arr5)}")