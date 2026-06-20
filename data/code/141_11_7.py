import numpy as np

def custom_and(a, b):
    return np.logical_and(a, b)

def custom_or(a, b):
    return np.logical_or(a, b)

def custom_not(a):
    return np.logical_not(a)

if __name__ == '__main__':
    a = np.array([True, False, True, False])
    b = np.array([False, False, True, True])
    
    and_result = custom_and(a, b)
    or_result = custom_or(a, b)
    not_result = custom_not(a)

    print("Custom AND:")
    print(and_result)
    print("\nCustom OR:")
    print(or_result)
    print("\nCustom NOT:")
    print(not_result)