import numpy as np

def custom_and(a, b):
    return np.logical_and(a, b)

def custom_or(a, b):
    return np.logical_or(a, b)

def custom_not(a):
    return np.logical_not(a)

if __name__ == '__main__':
    a = np.array([True, True, False, False])
    b = np.array([False, True, False, True])

    print("Custom AND:")
    result_and = custom_and(a, b)
    print(result_and)

    print("\nCustom OR:")
    result_or = custom_or(a, b)
    print(result_or)

    print("\nCustom NOT:")
    result_not_a = custom_not(a)
    result_not_b = custom_not(b)
    print(result_not_a)
    print(result_not_b)