import numpy as np

def custom_and(a, b):
    return np.logical_and(a, b)

def custom_or(a, b):
    return np.logical_or(a, b)

def custom_not(a):
    return np.logical_not(a)

if __name__ == '__main__':
    a = np.array([True, False, True, False])
    b = np.array([True, True, False, False])

    print("Custom AND:")
    print(custom_and(a, b))

    print("\nCustom OR:")
    print(custom_or(a, b))

    print("\nCustom NOT (a):")
    print(custom_not(a))